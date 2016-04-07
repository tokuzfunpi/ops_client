from ops_client.manager.base import BaseManager

class DesignateBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'dns_url'

    def _gen_content_type(self, _type = 'http', key = 'Content-Type', 
                          _headers = None) :
        if not _headers :
            headers = {}
        else :
            headers = _headers.copy()
        if _type == 'http' :
            content_type = 'application/json'
        elif _type == 'dns' :
            content_type = 'text/dns'
        else :
            content_type = ''
        headers[key] = content_type
        return headers

    def _handle_designate_header(self, kwargs):
        headers = kwargs.get('headers', {})
        _headers = self._gen_content_type(_headers = headers)
        _headers = self._gen_content_type(key = 'Accept', _headers = _headers)
        return _headers
