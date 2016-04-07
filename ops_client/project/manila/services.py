from ops_client.manager.manila import ManilaBaseManager
import six
try:
    from urllib import urlencode  # noqa
except ImportError:
    from urllib.parse import urlencode  # noqa

RESOURCES_PATH = '/os-services'


class ServiceManager(ManilaBaseManager):
    """Manage :class:`Service` resources."""

    def list(self, search_opts=None, **kwargs):
        """Get a list of all services.

        :rtype: list of :class:`Service`
        """
        query_string = ''
        if search_opts:
            query_string = urlencode(
                sorted([(k, v) for (k, v) in six.iteritems(search_opts) if v]))
            if query_string:
                query_string = "?%s" % query_string
        return self._get(RESOURCES_PATH + query_string, **kwargs)

    def enable_service(self, updates=None, **kwargs):
        if not updates:
            return
        return self._put("%s/enable" % RESOURCES_PATH, updates, **kwargs)

    def disable_service(self, updates=None, **kwargs):
        if not updates:
            return
        return self._put("%s/disable" % RESOURCES_PATH, updates, **kwargs)
