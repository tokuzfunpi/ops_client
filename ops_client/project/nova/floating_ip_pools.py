"""
Floating IP pools interface.
"""

from ops_client.manager.nova import NovaBaseManager

class FloatingIPPoolManager(NovaBaseManager):

    def list(self, response_key = True, **kwargs):
        """
        Retrieve a list of all floating ip pools.
        """
        if response_key :
            return self._get('/os-floating-ip-pools',
                             'floating_ip_pools', **kwargs)
        else :
            return self._get('/os-floating-ip-pools', **kwargs)
