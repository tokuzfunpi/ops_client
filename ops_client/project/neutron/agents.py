from ops_client.manager.neutron import NeutronBaseManager

class AgentManager(NeutronBaseManager):

    def list_agents(self, params = None, **kwargs):
        """List agents."""
        return self._get(self.agents_path, params=params, **kwargs)

    def show_agent(self, agent_id, params = None, **kwargs):
        """Show information of a given agent.

        :param agent_id: ID of the agent.
        """
        return self._get(self.agent_path % (agent_id), params=params, **kwargs)

    def update_agent(self, agent_id, update_body, **kwargs):
        """Update a given agent.

        :param agent_id: ID of the agent.
        :param update_body: update values.
        """
        body = {
            "agent" : update_body
        }
        return self._put(self.agent_path % (agent_id), body=body, **kwargs)

    def delete_agent(self, agent_id, **kwargs):
        """Delete a given agent.

        :param agent: ID of the agent.
        """
        return self._delete(self.agent_path % (agent_id), **kwargs)
