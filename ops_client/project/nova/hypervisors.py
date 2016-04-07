"""
Hypervisors interface.
"""

from six.moves.urllib import parse
from ops_client.manager.nova import NovaBaseManager

class HypervisorManager(NovaBaseManager):

    def list(self, detailed=True, response_key = True, **kwargs):
        """
        Get a list of hypervisors.
        """
        detail = ""
        if detailed:
            detail = "/detail"
        if response_key :
            return self._get('/os-hypervisors%s' % detail,
                             'hypervisors', **kwargs)
        else :
            return self._get('/os-hypervisors%s' % detail, **kwargs)

    def search(self, hypervisor_match, servers=False,
               response_key = True, **kwargs):
        """
        Get a list of matching hypervisors.

        :param servers: If True, server information is also retrieved.
        """
        target = 'servers' if servers else 'search'
        url = ('/os-hypervisors/%s/%s' %
               (parse.quote(hypervisor_match, safe=''), target))
        if response_key :
            return self._get(url, 'hypervisors', **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, hypervisor_id, response_key = True, **kwargs):
        """
        Get a specific hypervisor.
        """
        if response_key :
            return self._get("/os-hypervisors/%s" % hypervisor_id,
                             "hypervisor", **kwargs)
        else :
            return self._get("/os-hypervisors/%s" % hypervisor_id, **kwargs)

    def uptime(self, hypervisor_id, response_key = True, **kwargs):
        """
        Get the uptime for a specific hypervisor.
        """
        if response_key :
            return self._get("/os-hypervisors/%s/uptime" % hypervisor_id,
                             "hypervisor", **kwargs)
        else :
            return self._get("/os-hypervisors/%s/uptime" % hypervisor_id,
                             **kwargs)

    def statistics(self, response_key = True, **kwargs):
        """
        Get hypervisor statistics over all compute nodes.
        """
        if response_key :
            return self._get("/os-hypervisors/statistics",
                             "hypervisor_statistics", **kwargs)
        else :
            return self._get("/os-hypervisors/statistics", **kwargs)
