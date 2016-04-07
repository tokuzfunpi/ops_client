from ops_client.manager.neutron import NeutronBaseManager

class FloatingIPManager(NeutronBaseManager):

    def list_floatingips(self, params = None, **kwargs):
        """List floating IPs that belong to a given tenant."""
        return self._get(self.floatingips_path, params = params, **kwargs)

    def show_floatingip(self, floatingip_id, params = None, **kwargs):
        """Show information of a given floating IP.

        :param floatingip: ID of the floating ip.
        """
        return self._get(self.floatingip_path % (floatingip_id), 
                         params = params, **kwargs)

    def create_floatingip(self, floating_network_id = None, port_id = None, 
                          **kwargs):
        """Create a floating IP for a given tenant.

        :param floating_network_id: ID of the floating network.
        :param port_id: ID of the port.
        """
        body = {
            "floatingip":{
                "floating_network_id" : floating_network_id,
                "port_id" : port_id
            }
        }
        return self._post(self.floatingips_path, body=body, **kwargs)

    def update_floatingip(self, floatingip_id, update_body, **kwargs):
        """Update a floating IP for a given tenant.

        :param floatingip_id: ID of the floating ip.
        """
        body = {
            "floatingip" : update_body
        }
        return self._put(self.floatingip_path % (floatingip_id), body = body, 
                         **kwargs)

    def delete_floatingip(self, floatingip_id, **kwargs):
        """Delete a given floating IP.

        :param floatingip_id: ID of the floating ip.
        """
        return self._delete(self.floatingip_path % (floatingip_id), **kwargs)
