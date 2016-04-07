from ops_client.manager.sahara import SaharaBaseManager


class JobTypeManager(SaharaBaseManager):

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/job-types%s' % query_string
        return self._get(url, **kwargs)
