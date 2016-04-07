from ops_client.manager.neutron import NeutronBaseManager

class ServiceProviderManager(NeutronBaseManager):

    def list_service_providers(self, params = None):
        """Fetches service providers."""
        # Pass filters in "params" argument to do_request
        return self._get(self.service_providers_path, params=params)
