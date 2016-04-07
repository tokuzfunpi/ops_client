from ops_client.manager.base import BaseManager

class HeatBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'heat_url'

    def base_post(self, url, response_key = None, headers = {}, 
                  params = None, timeout = 60, content_type = None,
                  content_size = None, **kwargs):
        _headers = self._set_token(headers)
        url = self._update_final_url(url, params)
        resp, body = self.api.do_request(url, 'POST', _headers,
                                         timeout = timeout,
                                         content_type = content_type,
                                         content_size = content_size, 
                                         **kwargs)
        if response_key :
            return resp, body[response_key]
        else : 
            return resp, body