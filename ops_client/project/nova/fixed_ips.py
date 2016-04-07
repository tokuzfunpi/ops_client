"""
Fixed IPs interface. (For nova-network)
"""

from ops_client.manager.nova import NovaBaseManager

class FixedIPsManager(NovaBaseManager):

    def get(self, fixed_ip_id, response_key = True, **kwargs):
        """
        Show information for a Fixed IP

        :param fixed_ip: Fixed IP address to get info for
        """
        if response_key :
            return self._get('/os-fixed-ips/%s' % fixed_ip_id,
                             "fixed_ip", **kwargs)
        else :
            return self._get('/os-fixed-ips/%s' % fixed_ip_id, **kwargs)

    def reserve(self, fixed_ip_id, **kwargs):
        """Reserve a Fixed IP

        :param fixed_ip: Fixed IP address to reserve
        """
        body = {"reserve": None}
        return self._post('/os-fixed-ips/%s/action' %
                          fixed_ip_id, body, **kwargs)

    def unreserve(self, fixed_ip_id, **kwargs):
        """Unreserve a Fixed IP

        :param fixed_ip: Fixed IP address to unreserve
        """
        body = {"unreserve": None}
        return self._post('/os-fixed-ips/%s/action' % 
                          fixed_ip_id, body, **kwargs)
