from ops_client.manager.neutron import NeutronBaseManager

class NetworkGatewayManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    def list_network_gateways(self, params = None):
        """Retrieve network gateways."""
        return self._get(self.network_gateways_path, params=params)

    def show_network_gateway(self, gateway_id, params = None):
        """Fetch a network gateway."""
        return self._get(self.network_gateway_path % gateway_id, params=params)

    def create_network_gateway(self, body=None):
        """Create a new network gateway."""
        return self._post(self.network_gateways_path, body=body)

    def update_network_gateway(self, gateway_id, body=None):
        """Update a network gateway."""
        return self._put(self.network_gateway_path % gateway_id, body=body)

    def delete_network_gateway(self, gateway_id):
        """Delete the specified network gateway."""
        return self._delete(self.network_gateway_path % gateway_id)

    def connect_network_gateway(self, gateway_id, body=None):
        """Connect a network gateway to the specified network."""
        base_uri = self.network_gateway_path % gateway_id
        return self._put("%s/connect_network" % base_uri, body=body)

    def disconnect_network_gateway(self, gateway_id, body=None):
        """Disconnect a network from the specified gateway."""
        base_uri = self.network_gateway_path % gateway_id
        return self._put("%s/disconnect_network" % base_uri, body=body)
