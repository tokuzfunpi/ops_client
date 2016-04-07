from ops_client.manager.neutron import NeutronBaseManager

class FirewallRuleManager(NeutronBaseManager):
    """
    .. warning::

       Create firewall rule is the first step for create firewall.
    """

    def list_firewall_rules(self, params = None):
        """List firewall rules that belong to a given tenant."""
        return self._get(self.firewall_rules_path, params=params)

    def show_firewall_rule(self, firewall_rule, params = None):
        """Show information of a given firewall rule.

        :param firewall_rule: ID of the firewall rule.
        """
        return self._get(self.firewall_rule_path % (firewall_rule),
                        params=params)

    def create_firewall_rule(self, **kwargs):
        """Create a firewall rule.

        :param kwarg: firewall rule values.
        """
        body = {
            "firewall_rule":kwargs
        }
        return self._post(self.firewall_rules_path, body=body)

    def update_firewall_rule(self, firewall_rule,
                             fw_rule_body = None, **kwargs):
        """Update a given firewall rule.

        :param firewall_rule: ID of the firewall rule.
        """
        _body = {}
        if fw_rule_body and type(fw_rule_body) == dict :
            _body.update(fw_rule_body)
        body = {"firewall_rule":_body}
        return self._put(self.firewall_rule_path % (firewall_rule), body=body)

    def delete_firewall_rule(self, firewall_rule):
        """Delete a given firewall rule.

        :param firewall_rule: ID of the firewall rule.
        """
        return self._delete(self.firewall_rule_path % (firewall_rule))
