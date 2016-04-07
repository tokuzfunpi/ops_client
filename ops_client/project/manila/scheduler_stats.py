from ops_client.manager.manila import ManilaBaseManager
import six.moves.urllib.parse as urlparse

RESOURCES_PATH = '/scheduler-stats/pools'


class PoolManager(ManilaBaseManager):
    """Manage :class:`Pool` resources."""

    def list(self, detailed=True, search_opts=None, **kwargs):
        """Get a list of pools.

        :rtype: list of :class:`Pool`
        """
        if search_opts is None:
            search_opts = {}

        if search_opts:
            query_string = urlparse.urlencode(
                sorted([(k, v) for (k, v) in list(search_opts.items()) if v]))
            if query_string:
                query_string = "?%s" % (query_string,)
        else:
            query_string = ''

        if detailed:
            path = '%(resources_path)s/detail%(query)s' % {
                'resources_path': RESOURCES_PATH,
                'query': query_string
            }
        else:
            path = '%(resources_path)s%(query)s' % {
                'resources_path': RESOURCES_PATH,
                'query': query_string
            }

        return self._get(path, **kwargs)
