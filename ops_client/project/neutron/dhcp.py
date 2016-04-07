from ops_client.manager.neutron import NeutronBaseManager

class DHCPManager(NeutronBaseManager):

    def list_dhcp_agent_hosting_networks(self, network, params = None, 
                                         **kwargs):
        """List DHCP agents hosting a network.

        :param network: ID of the network.
        """
        return self._get((self.network_path + self.DHCP_AGENTS) % network,
                        params=params, **kwargs)

    def list_networks_on_dhcp_agent(self, dhcp_agent, params = None, **kwargs):
        """List the networks on a DHCP agent.

        :param dhcp_agent: ID of the DHCP-agent.
        """
        return self._get((self.agent_path + self.DHCP_NETS) % dhcp_agent,
                        params=params, **kwargs)

    def add_network_to_dhcp_agent(self, dhcp_agent, network_id, **kwargs):
        """Add a network to a DHCP agent.

        :param dhcp_agent: ID of the DHCP-agent.
        :param network: ID of the network.
        """
        body = {"network_id":network_id}
        return self._post((self.agent_path + self.DHCP_NETS) % dhcp_agent,
                         body=body, **kwargs)

    def remove_network_from_dhcp_agent(self, dhcp_agent, network_id, **kwargs):
        """Remove a network from a DHCP agent.

        :param dhcp_agent: ID of the DHCP-agent.
        :param network: ID of the network.
        """
        return self._delete((self.agent_path + self.DHCP_NETS + "/%s") % (
            dhcp_agent, network_id), **kwargs)
