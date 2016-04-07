"""
Virtual Interfaces (For nova-network).
"""

from ops_client.manager.nova import NovaBaseManager

class VirtualInterfaceManager(NovaBaseManager):

    def list(self, instance_id, response_key = True, **kwargs):
        if response_key :
            return self._get('/servers/%s/os-virtual-interfaces' % instance_id,
                              'virtual_interfaces', **kwargs)
        else :
            return self._get('/servers/%s/os-virtual-interfaces' % instance_id,
                              **kwargs)