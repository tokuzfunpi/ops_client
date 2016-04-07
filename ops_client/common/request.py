import httplib
from urlparse import urlparse
from ops_client.common.utils import AttributeDict
from ops_client.common import exception
import json
import base64
import os

def do_request(url, method = 'GET', headers = {}, contents = None,
               chunk_size = 65536, content_size = None, read = True, 
               timeout = 60, json_parse = True, content_type = None, 
               auth_user = None, auth_pwd = None, **kwargs):
    _u = urlparse(url)
    if _u.scheme == 'http' :
        conn = httplib.HTTPConnection(_u.hostname, _u.port, timeout = timeout)
    elif _u.scheme == 'https' :
        conn = httplib.HTTPConnection(_u.hostname, _u.port, timeout = timeout)
    else :
        raise Exception('Wrong URL')
    if content_size :
        headers['Content-Length'] = content_size
    elif contents and not content_size :
        if hasattr(contents, 'read'):
            try :
                headers['Content-Length'] = os.fstat(contents.fileno()).st_size
            except Exception :
                headers['Content-Length'] = 0
        else :
            headers['Content-Length'] = len(contents)
    else :
        headers['Content-Length'] = content_size or 0

    if content_type :
        headers['Content-Type'] = content_type

    _url = _u.path + '?' + _u.query
    #Basic auth/pwd case
    if auth_user and auth_pwd :
        auth_info = base64.encodestring('%s:%s' % \
                                        (auth_user, auth_pwd)).replace('\n', '')
        headers["Authorization"] = "Basic %s" % auth_info
    try :
        if contents :
            if hasattr(contents, 'read'):
                headers['Content-Type'] = 'application/octet-stream'
                conn.putrequest(method, _url)
                for header, value in headers.iteritems():
                    conn.putheader(str(header), str(value))
                conn.endheaders()
                chunk = contents.read(65536)
                while chunk:
                    conn.send(chunk)
                    chunk = contents.read(65536)
            else:
                conn.request(method, _url, contents, headers)
        else :
            conn.request(method, _url, contents, headers)
    except Exception as err:
        pass
    finally :
        try :
            resp = conn.getresponse()
        except Exception :
            raise exception.ServiceUnavailable()

    _headers = {}
    for header, value in resp.getheaders():
        _headers[header] = value
    _resp = {'status' : resp.status, 'headers' : _headers}
    _resp = AttributeDict(_resp)
    if resp.status >= 400 :
        raise exception.from_response(_resp, resp.read(), method, url)

    if read and json_parse :
        json_body = None
        try :
            _body = resp.read()
            json_body = json.loads(_body)
        except Exception :
            pass
        return _resp, json_body
    elif read and not json_parse :
        return _resp, resp.read()
    else :
        return _resp, resp
