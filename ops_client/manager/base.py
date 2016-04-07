from ops_client.decorator.base import check_token, check_target_url
from ops_client.common.utils import json_dump

class BaseManager():

    def _set_token(self, headers):
        _headers = headers.copy()
        if not headers.get('X-Replace-Token') :
            _headers['X-Auth-Token'] = self.api.token
        else :
            _headers['X-Auth-Token'] = headers.get('X-Replace-Token')
        return _headers

    def _update_final_url(self, orig_url, params = None):
        self.target_url = getattr(self.api, self.url_type, None)
        _url = self.api.concat_url(self.target_url, orig_url)
        if params :
            _url = self.api.add_query_string(_url, params)
        return _url

    def _get_request_body(self, body, headers):
        if body is None :
            return None, headers
        _body = body
        if not hasattr(body, 'read'):
            headers['Content-Type'] = 'application/json'
            if type(body) == list or type(body) == dict :
                try :
                    _body = json_dump(body)
                except Exception :
                    _body = body
        return _body

    @check_token
    @check_target_url
    def _get(self, url, response_key = None, headers = {}, params = None, 
             timeout = 60, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        resp, body = self.api.do_request(url, 'GET', _headers, 
                                         timeout = timeout, **kwargs)
        if response_key :
            return resp, body[response_key]
        else : 
            return resp, body

    @check_token
    @check_target_url
    def _head(self, url, headers = {}, params = None, timeout = 60, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        resp, junk = self.api.do_request(url, 'HEAD', _headers, 
                                         timeout = timeout, **kwargs)
        return resp, None

    @check_token
    @check_target_url
    def _post(self, url, body, response_key = None, headers = {}, 
              params = None, timeout = 60, content_type = None,
              content_size = None, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        _body = self._get_request_body(body, _headers)
        resp, body = self.api.do_request(url, 'POST', _headers,
                                         contents = _body, timeout = timeout,
                                         content_type = content_type,
                                         content_size = content_size, 
                                         **kwargs)
        if response_key :
            return resp, body[response_key]
        else : 
            return resp, body

    @check_token
    @check_target_url
    def _put(self, url, body = None, response_key = None, headers = {}, 
             params = None, timeout = 60, content_type = None,
             content_size = None, **kwargs):
        return self._put_or_patch(url, body, response_key, headers, params,
                                  'PUT', timeout, content_type,
                                  content_size, **kwargs)

    @check_token
    @check_target_url
    def _patch(self, url, body = None, response_key=None,  headers = {}, 
               params = None, timeout = 60, content_type = None,
               content_size = None, **kwargs):
        return self._put_or_patch(url, body, response_key, headers, params,
                                  'PATCH', timeout, content_type, 
                                  content_size, **kwargs)
        

    def _put_or_patch(self, url, body = None, response_key=None,  headers = {}, 
                      params = None, method = 'PUT', timeout = 60, 
                      content_type = None, content_size = None, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        if body :
            _body = self._get_request_body(body, _headers)
        else :
            _body =None
        resp, body = self.api.do_request(url, method, _headers, 
                                         contents = _body, timeout = timeout,
                                         content_type = content_type,
                                         content_size = content_size, **kwargs)
        if body and response_key :
            return resp, body[response_key]
        elif body and not response_key :
            return resp, body
        else:
            return resp, None

    @check_token
    @check_target_url
    def _delete(self, url, headers = {}, params = None, timeout = 60, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        return self.api.do_request(url, 'DELETE', _headers, timeout = timeout, 
                                   **kwargs)
    
