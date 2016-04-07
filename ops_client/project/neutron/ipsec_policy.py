from ops_client.manager.neutron import NeutronBaseManager

class IpsecPolicyManager(NeutronBaseManager):

    def list_ipsecpolicies(self, params = None):
        """Fetches a list of all configured IPsecPolicies for a tenant."""
        return self._get(self.ipsecpolicies_path, params=params)

    def show_ipsecpolicy(self, ipsecpolicy, params = None):
        """Fetches information of a specific IPsecPolicy.

        :param ipsecpolicy: ID of the ipsecpolicy.
        """
        return self._get(self.ipsecpolicy_path % (ipsecpolicy), params=params)

    def create_ipsecpolicy(self, body = None, **kwargs):
        """Creates a new IPsecPolicy.

        :param kwargs: ipsecpolicy values.
        """
        _body = {}
        if body and type(body) == dict :
            _body.update(body)
        body = {"ipsecpolicy":_body}
        return self._post(self.ipsecpolicies_path, body=body)

    def update_ipsecpolicy(self, ipsecpolicy, body = None, **kwargs):
        """Updates an IPsecPolicy.

        :param ipsecpolicy: ID of the ipsecpolicy.
        :param kwargs: update values.
        """
        _body = {}
        if body and type(body) == dict :
            _body.update(body)
        body = {"ipsecpolicy" : _body}
        return self._put(self.ipsecpolicy_path % (ipsecpolicy), body=body)

    def delete_ipsecpolicy(self, ipsecpolicy):
        """Deletes the specified IPsecPolicy.

        :param ipsecpolicy: ID of the ipsecpolicy.
        """
        return self._delete(self.ipsecpolicy_path % (ipsecpolicy))
