from ops_client.manager.trove import TroveBaseManager

class RootManager(TroveBaseManager):

    def _create(self, url, response_key = None, headers = {}, 
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

    def create(self, instance, **kwargs):
        """Implements root-enable API.

        Enable the root user and return the root password for the
        specified db instance.
        """
        return self._create("/instances/%s/root" % instance, **kwargs)

    def is_root_enabled(self, instance, response_key = True, **kwargs):
        """Return whether root is enabled for the instance."""

        return self._get("/instances/%s/root" % instance, **kwargs)
