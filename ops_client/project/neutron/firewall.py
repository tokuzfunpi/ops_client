from ops_client.manager.neutron import NeutronBaseManager

class FirewallManager(NeutronBaseManager):
    """
    .. warning::

       Create firewall after create firewall policy.
    """

    def list_firewalls(self, params = None):
        """List firewalls that belong to a given tenant."""
        return self._get(self.firewalls_path, params=params)

    def show_firewall(self, firewall, params = None):
        """Show information of a given firewall."""
        return self._get(self.firewall_path % (firewall), params=params)

    def create_firewall(self, fw_policy_id):
        """Create a firewall.

        :param fw_policy_id: ID of the firewall policy.
        """
        body = {
            "firewall":{
                "firewall_policy_id":fw_policy_id
            }
        }
        return self._post(self.firewalls_path, body=body)

    def update_firewall(self, firewall, **kwargs):
        """Update a given firewall.

        :param firewall: ID of the firewall.
        :param kwargs: Update values.
        """
        body = {
            "firewall":kwargs
        }
        return self._put(self.firewall_path % (firewall), body=body)

    def delete_firewall(self, firewall):
        """Delete a given firewall.

        :param firewall: ID of the firewall.
        """
        return self._delete(self.firewall_path % (firewall))
