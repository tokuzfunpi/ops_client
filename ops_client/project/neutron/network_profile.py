from ops_client.manager.neutron import NeutronBaseManager

class NetworkProfileManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    # def list_network_profile_bindings(self, params = None):
    #     """Fetch a list of all tenants associated for a network profile."""
    #     return self._get(self.network_profile_bindings_path, params=params)

    def list_network_profiles(self, params = None):
        """Fetch a list of all network profiles for a tenant."""
        return self._get(self.network_profiles_path, params=params)

    def show_network_profile(self, profile, params = None):
        """Fetch a network profile."""
        return self._get(self.network_profile_path % (profile), params=params)

    def create_network_profile(self, body=None):
        """Create a network profile."""
        return self._post(self.network_profiles_path, body=body)

    def update_network_profile(self, profile, body=None):
        """Update a network profile."""
        return self._put(self.network_profile_path % (profile), body=body)

    def delete_network_profile(self, profile):
        """Delete the network profile."""
        return self._delete(self.network_profile_path % profile)
