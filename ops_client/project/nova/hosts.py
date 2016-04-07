"""
host interface.
"""

from ops_client.manager.nova import NovaBaseManager

class HostManager(NovaBaseManager):

    def get(self, host, response_key = True, **kwargs):
        """
        Describes cpu/memory/hdd info for host.

        :param host: destination host name.
        """
        if response_key :
            return self._get("/os-hosts/%s" % host, "host", **kwargs)
        else :
            return self._get("/os-hosts/%s" % host, **kwargs)

    def update(self, host, values, **kwargs):
        """Update status or maintenance mode for the host."""
        if type(values) is dict:
            return self._put("/os-hosts/%s" % host, values, **kwargs)
        else:
            raise TypeError('Value Type should be dict.')

    def host_action(self, host, action, **kwargs):
        """Perform an action on a host."""
        url = '/os-hosts/{0}/{1}'.format(host, action)
        return self._get(url, **kwargs)

    def list(self, zone = None, response_key = True, **kwargs):
        url = '/os-hosts'
        if zone:
            url = '/os-hosts?zone=%s' % zone
        if response_key : 
            return self._get(url, "hosts", **kwargs)
        else :
            return self._get(url, **kwargs)
