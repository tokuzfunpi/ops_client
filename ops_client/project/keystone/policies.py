from ops_client.manager.keystone import KeystoneBaseManager

class PolicyManager(KeystoneBaseManager):
    """Represents an Identity policy.

    Attributes:
        * id: a uuid that identifies the policy
        * blob: a policy document (blob)
        * type: the mime type of the policy blob

    """
    collection_key = 'policies'
    key = 'policy'

    def create_policy(self, blob, type = 'application/json'):
        return self.create(blob = blob, type = type)

    def get_policy(self, policy_id):
        return self.get(policy_id = policy_id)

    def list_policy(self):
        """List policies.

        ``**kwargs`` allows filter criteria to be passed where
         supported by the server.
        """
        return self.list()

    def update_policy(self, policy_id, blob = None, type = None):
        return self.update(
            policy_id = policy_id,
            blob=blob,
            type=type)

    def delete_policy(self, policy_id):
        return self.delete(policy_id = policy_id)
