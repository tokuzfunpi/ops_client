from ops_client.manager.neutron import NeutronBaseManager

class PolicyProfileManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    # def list_policy_profile_bindings(self, params = None):
    #     """Fetch a list of all tenants associated for a policy profile."""
    #     return self._get(self.policy_profile_bindings_path, params=params)

    def list_policy_profiles(self, params = None):
        """Fetch a list of all network profiles for a tenant."""
        return self._get(self.policy_profiles_path, params=params)

    def show_policy_profile(self, profile, params = None):
        """Fetch a network profile."""
        return self._get(self.policy_profile_path % (profile), params=params)

    def update_policy_profile(self, profile, body=None):
        """Update a policy profile."""
        return self._put(self.policy_profile_path % (profile), body=body)
