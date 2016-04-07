from ops_client.manager.keystone import KeystoneBaseManager

class DomainManager(KeystoneBaseManager):
    """Represents an Identity domain.

    Attributes:
        * id: a uuid that identifies the domain

    """
    collection_key = 'domains'
    key = 'domain'

    def create_domain(self, name, description = None, enabled = True):
        return self.create(
            name=name,
            description=description,
            enabled=enabled)

    def get_domain(self, domain_id):
        return self.get(
            domain_id = domain_id)

    def list_domain(self):
        """List domains.

        ``**kwargs`` allows filter criteria to be passed where
         supported by the server.
        """
        return self.list()

    def update_domain(self, domain_id, name = None, description = None, 
                      enabled = True):
        return self.update(
            domain_id = domain_id,
            name = name,
            description = description,
            enabled = enabled)

    def delete_domain(self, domain_id):
        return self.delete(domain_id = domain_id)
