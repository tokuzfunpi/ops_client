from ops_client.manager.keystone import KeystoneBaseManager

class ServiceManager(KeystoneBaseManager):
    """Represents an Identity service.

    Attributes:
        * id: a uuid that identifies the service
        * name: user-facing name of the service (e.g. Keystone)
        * type: 'compute', 'identity', etc
        * enabled: determines whether the service appears in the catalog

    """
    collection_key = 'services'
    key = 'service'

    def create_service(self, name, type, enabled = True, **kwargs):
        return self.create(
            name=name,
            type=type,
            enabled=enabled,
            **kwargs)

    def get_service(self, service_id):
        return self.get(service_id = service_id)

    def update_service(self, service_id, name = None, type = None, 
                        enabled = None, **kwargs):
        return self.update(
            service_id = service_id,
            name=name,
            type=type,
            enabled=enabled,
            **kwargs)

    def delete_service(self, service_id):
        return self.delete(service_id = service_id)
