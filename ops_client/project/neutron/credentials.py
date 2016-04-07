from ops_client.manager.neutron import NeutronBaseManager

class CredentialsManager(NeutronBaseManager):

    """
    .. warning:
       For cisco plugins
    """
    def list_credentials(self, params = None, **kwargs):
        """Fetch a list of all credentials for a tenant."""
        return self._get(self.credentials_path, params=params, **kwargs)

    def show_credential(self, credential, params = None, **kwargs):
        """Fetch a credential."""
        return self._get(self.credential_path % (credential), params=params,
                         **kwargs)

    def create_credential(self, body=None, **kwargs):
        """Create a new credential."""
        return self._post(self.credentials_path, body=body, **kwargs)

    # def update_credential(self, credential, body=None, **kwargs):
    #     """Update a credential."""
    #     return self._put(self.credential_path % (credential), body=body, 
    #                      **kwargs)

    def delete_credential(self, credential, **kwargs):
        """Delete the specified credential."""
        return self._delete(self.credential_path % (credential), **kwargs)
