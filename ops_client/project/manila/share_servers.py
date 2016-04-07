from ops_client.manager.manila import ManilaBaseManager
from ops_client.common import manila_constants as constants
import collections
import six
try:
    from urllib import urlencode  # noqa
except ImportError:
    from urllib.parse import urlencode  # noqa

RESOURCES_PATH = '/share-servers'
RESOURCE_PATH = '/share-servers/%s'
RESOURCES_NAME = 'share_servers'
RESOURCE_NAME = 'share_server'


class ShareServerManager(ManilaBaseManager):
    """Manage :class:`ShareServer` resources."""

    def get(self, server_id):
        """Get a share server.

        :param server_id: The ID of the share server to get.
        :rtype: :class:`ShareServer`
        """
        server = self._get("%s/%s" % (RESOURCES_PATH, server_id),
                           RESOURCE_NAME)
        # Split big dict 'backend_details' to separated strings
        # as next:
        # +---------------------+------------------------------------+
        # |       Property      |                Value               |
        # +---------------------+------------------------------------+
        # | details:instance_id |35203a78-c733-4b1f-b82c-faded312e537|
        # +---------------------+------------------------------------+
        for k, v in six.iteritems(server._info["backend_details"]):
            server._info["details:%s" % k] = v
        return server

    def details(self, server_id):
        """Get a share server details.

        :param server_id: The ID of the share server to get details from.
        :rtype: list of :class:`ShareServerBackendDetails
        """
        return self._get("%s/%s/details" % (RESOURCES_PATH, server_id),
                         "details")

    def delete(self, server_id):
        """Delete share server.

        :param server_id: id of share server to be deleted.
        """
        self._delete(RESOURCE_PATH % server_id)

    def list(self, search_opts=None, **kwargs):
        """Get a list of share servers.

        :rtype: list of :class:`ShareServer`
        """
        query_string = ''
        if search_opts:
            opts = sorted(
                [(k, v) for (k, v) in six.iteritems(search_opts) if v])
            query_string = urlencode(opts)
            query_string = '?' + query_string if query_string else ''
        return self._get(RESOURCES_PATH + query_string, **kwargs)
