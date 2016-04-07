from ops_client.manager.keystone import KeystoneBaseManager

VALID_INTERFACES = ['public', 'admin', 'internal', 'secure']

class EndpointManager(KeystoneBaseManager):
    """Represents an Identity endpoint.

    Attributes:
        * id: a uuid that identifies the endpoint
        * interface: 'public', 'admin' or 'internal' network interface
        * region: geographic location of the endpoint
        * service_id: service to which the endpoint belongs
        * url: fully qualified service endpoint
        * enabled: determines whether the endpoint appears in the catalog

    """
    collection_key = 'endpoints'
    key = 'endpoint'

    def _validate_interface(self, interface):
        if interface is not None and interface not in VALID_INTERFACES:
            msg = '"interface" must be one of: %s'
            msg = msg % ', '.join(VALID_INTERFACES)
            raise Exception(msg)

    def create_endpoint(self, service_id, url, interface = None, region = None, 
               enabled = True, **kwargs):
        self._validate_interface(interface)
        return self.create(
            service_id = service_id,
            interface = interface,
            url = url,
            region = region,
            enabled = enabled,
            **kwargs)

    def get_endpoint(self, endpoint_id):
        return self.get(endpoint_id = endpoint_id)

    def list_endpoint(self, service_id = None, interface = None, region = None, 
                      enabled = None, **kwargs):
        """List endpoints.

        If ``**kwargs`` are provided, then filter endpoints with
        attributes matching ``**kwargs``.
        """
        self._validate_interface(interface)
        return self.list(
            service_id = service_id,
            interface = interface,
            region = region,
            enabled = enabled,
            **kwargs)

    def update_endpoint(self, endpoint_id, service_id = None, url = None, 
                        interface = None, region = None, enabled = None,
                        **kwargs):
        self._validate_interface(interface)
        return self.update(
            endpoint_id = endpoint_id,
            service_id = service_id,
            interface = interface,
            url = url,
            region = region,
            enabled = enabled,
            **kwargs)

    def delete_endpoint(self, endpoint_id):
        return self.delete(endpoint_id = endpoint_id)
