from ops_client.manager.base import BaseManager

class TroveBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'trove_url'

    def build_url(self, url, limit=None, marker=None, query_strings=None):

        def append_query_strings(url, **query_strings):
            if not query_strings:
                return url
            query = '&'.join('{0}={1}'.format(key, val)
                             for key, val in query_strings.items() if val)
            return url + ('?' + query if query else "")

        query_strings = query_strings or {}
        url = append_query_strings(url, limit = limit, marker = marker,
                                   **query_strings)

        return url
