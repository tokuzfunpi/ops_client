from ops_client.manager.neutron import NeutronBaseManager

class IKEPolicyManager(NeutronBaseManager):

    def list_ikepolicies(self, params = None):
        """Fetches a list of all configured IKEPolicies for a tenant."""
        return self._get(self.ikepolicies_path, params=params)

    def show_ikepolicy(self, ikepolicy, params = None):
        """Fetches information of a specific IKEPolicy.

        :param ikepolicy: ID of the ikepolicy.
        """
        return self._get(self.ikepolicy_path % (ikepolicy), params=params)

    def create_ikepolicy(self, ikepolicy_body = None, **kwargs):
        """Creates a new IKEPolicy.

        :param kwargs: ikepolicy values.
        """
        _body = {}
        if ikepolicy_body and type(ikepolicy_body) == dict :
            _body.update(ikepolicy_body)
        body = {"ikepolicy":_body}
        return self._post(self.ikepolicies_path, body=body)

    def update_ikepolicy(self, ikepolicy, ikepolicy_body = None, **kwargs):
        """Updates an IKEPolicy.

        :param ikepolicy: ID of the ikepolicy.
        :param kwargs: update values.
        """
        _body = {}
        if ikepolicy_body and type(ikepolicy_body) == dict :
            _body.update(ikepolicy_body)
        body = {"ikepolicy":_body}
        return self._put(self.ikepolicy_path % (ikepolicy), body=body)

    def delete_ikepolicy(self, ikepolicy):
        """Deletes the specified IKEPolicy.

        :param ikepolicy: ID of the ikepolicy.
        """
        return self._delete(self.ikepolicy_path % (ikepolicy))
