from ops_client.manager.neutron import NeutronBaseManager

class FirewallPolicyManager(NeutronBaseManager):
    """
    .. warning::

       Create firewall policy after create firewall rule.
    """

    def list_firewall_policies(self, params = None):
        """List firewall policies that belong to a given tenant."""
        return self._get(self.firewall_policies_path, params=params)

    def show_firewall_policy(self, firewall_policy, params = None):
        """Show information of a given firewall policy.

        :param firewall_policy: ID of the firewall_policy.
        """
        return self._get(self.firewall_policy_path % (firewall_policy),
                        params=params)

    def create_firewall_policy(self, **kwargs):
        """Create a firewall policy.

        :param kwargs: firewall policy values.
        """
        body = {
            "firewall_policy":kwargs
        }
        return self._post(self.firewall_policies_path, body=body)

    def update_firewall_policy(self, firewall_policy,
                               fw_policy_body = None, **kwargs):
        """Update a given firewall policy.

        :param firewall_policy: ID of the firewall_policy.
        :param kwargs: update values.
        """
        _body = {}
        if fw_policy_body and type(fw_policy_body) == dict :
            _body.update(fw_policy_body)
        body = {"firewall_policy":_body}
        return self._put(self.firewall_policy_path % (firewall_policy),
                        body=body)

    def delete_firewall_policy(self, firewall_policy):
        """Delete a given firewall policy.

        :param firewall_policy: ID of the firewall_policy.
        """
        return self._delete(self.firewall_policy_path % (firewall_policy))

    def firewall_policy_insert_rule(self, firewall_policy, fw_rule_id):
        """Insert a rule into a given firewall policy.

        :param firewall_policy: ID of the firewall_policy.
        :param fw_rule_id: ID of the firewall rule.
        """
        body = {
            "firewall_rule_id":fw_rule_id
        }
        return self._put(self.firewall_policy_insert_path % (firewall_policy),
                        body=body)

    def firewall_policy_remove_rule(self, firewall_policy, fw_rule_id):
        """Remove a rule from a given firewall policy.

        :param firewall_policy: ID of the firewall_policy.
        :param fw_rule_id: ID of the firewall rule.
        """
        body = {
            "firewall_rule_id":fw_rule_id
        }
        return self._put(self.firewall_policy_remove_path % (firewall_policy),
                        body=body)
