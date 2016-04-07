from ops_client.manager.neutron import NeutronBaseManager

class GatewayDeviceManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    def list_gateway_devices(self, params = None):
        """Retrieve gateway devices."""
        return self._get(self.gateway_devices_path, params=params)

    def show_gateway_device(self, gateway_device_id, params = None):
        """Fetch a gateway device."""
        return self._get(self.gateway_device_path % gateway_device_id,
                        params=params)

    def create_gateway_device(self, body=None):
        """Create a new gateway device."""
        return self._post(self.gateway_devices_path, body=body)

    def update_gateway_device(self, gateway_device_id, body=None):
        """Updates a new gateway device."""
        return self._put(self.gateway_device_path % gateway_device_id,
                        body=body)

    def delete_gateway_device(self, gateway_device_id):
        """Delete the specified gateway device."""
        return self._delete(self.gateway_device_path % gateway_device_id)
