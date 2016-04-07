from ops_client.manager.keystone import KeystoneBaseManager

class CredentialManager(KeystoneBaseManager):
    """Represents an Identity credential.

    Attributes:
        * id: a uuid that identifies the credential

    """
    collection_key = 'credentials'
    key = 'credential'

    def create_credential(self, user_id, type, data, project_id = None):
        return self.create(
            user_id = user_id,
            type = type,
            data = data,
            project_id = project_id)

    def get_credential(self, credential_id):
        return self.get(
            credential_id = credential_id)

    def list_credential(self):
        """List credentials.

        If ``**kwargs`` are provided, then filter credentials with
        attributes matching ``**kwargs``.
        """
        return self.list()

    def update_credential(self, credential_id, user_id, type = None,
                          data = None, project_id = None):
        return self.update(
            credential_id = credential_id,
            user_id = user_id,
            type = type,
            data = data,
            project_id = project_id)

    def delete_credential(self, credential_id):
        return self.delete(
            credential_id = credential_id)
