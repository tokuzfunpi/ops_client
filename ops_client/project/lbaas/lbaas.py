from ops_client.manager.lbaas import LBaaSBaseManager

class LBaaSManager(LBaaSBaseManager):

    def get_lbaas_agent_hosting_pool(self, pool, prefix = '', params = None):
        """Fetches a loadbalancer agent hosting a pool.

        :param pool: ID of the pool.
        """
        url = prefix + (self.pool_path + self.LOADBALANCER_AGENT)
        return self.base_show(
            obj_info = {'pool' : pool}, 
            resource_url = url,
            params = params)

    def list_pools_on_lbaas_agent(self, lbaas_agent, prefix = '', params = None):
        """Fetches a list of pools hosted by the loadbalancer agent.

        :param lbaas_agent: ID of the LBaaS-Agent.
        """
        url = prefix + (self.agent_path + self.LOADBALANCER_POOLS)
        return self.base_show(
            obj_info = {'agent' : lbaas_agent},
            resource_url = url,
            params = params)
