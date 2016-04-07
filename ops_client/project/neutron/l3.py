from ops_client.manager.neutron import NeutronBaseManager

class L3Manager(NeutronBaseManager):

    def list_l3_agent_hosting_routers(self, router, params = None):
        """Fetches a list of L3 agents hosting a router.

        :param router: ID of the router.
        """
        return self._get((self.router_path + self.L3_AGENTS) % router,
                        params=params)

    def list_routers_on_l3_agent(self, l3_agent, params = None):
        """Fetches a list of L3 agents hosting a router.

        :param l3_agent: ID of the L3-Agent.
        """
        return self._get((self.agent_path + self.L3_ROUTERS) % l3_agent,
                        params=params)

    def add_router_to_l3_agent(self, l3_agent, router_id):
        """Add a router to a L3 agent.

        :param l3_agent: ID of the L3-Agent.
        :param router_id: ID of the router.
        """
        body = {"router_id":router_id}
        return self._post((self.agent_path + self.L3_ROUTERS) % l3_agent,
                         body=body)

    def remove_router_from_l3_agent(self, l3_agent, router_id):
        """Remove a router from l3 agent.

        :param l3_agent: ID of the L3-Agent.
        :param router_id: ID of the router.
        """
        return self._delete((self.agent_path + self.L3_ROUTERS + "/%s") % (
            l3_agent, router_id))
