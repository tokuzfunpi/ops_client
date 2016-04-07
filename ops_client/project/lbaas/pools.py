from ops_client.manager.lbaas import LBaaSBaseManager

class PoolManager(LBaaSBaseManager):

    def list_pools(self, prefix = '', params = None, **kwargs):
        """Fetches a list of all load balancer pools for a tenant."""
        # Pass filters in "params" argument to do_request
        url = prefix + self.pools_path
        return self.base_list(resource_url = url,
                              params = params,
                              **kwargs)

    def show_pool(self, pool, prefix = '', params = None, **kwargs):
        """Fetches information of a certain load balancer pool.

        :param pool: ID of the pool.
        """
        url = prefix + self.pool_path
        return self.base_show(obj_info = {'pool' : pool},
                              resource_url = url,
                              params=params,
                              **kwargs)

    def create_pool(self, lb_method, protocol, subnet, 
                    prefix = '', pool_body = None, **kwargs):
        """Creates a new load balancer pool.

        :param lb_method: 'ROUND_ROBIN',
        :param protocol: 'TCP','HTTP','HTTPS'
        :param subnet: ID of the subnet.
        """
        _body = {
            "lb_method":lb_method,
            "protocol":protocol,
            "subnet_id":subnet        
        }
        if pool_body and type(pool_body) == dict :
            _body.update(pool_body)
        body = {"pool":_body}
        url = prefix + self.pools_path
        return self.base_create(resource_url = url,
                                body = body,
                                **kwargs)

    def update_pool(self, pool, prefix = '', pool_body = None, **kwargs):
        """Updates a load balancer pool.

        :param pool: ID of the pool.
        :param kwargs: update value.
        """
        _body = {}
        if pool_body and type(pool_body) == dict :
            _body.update(pool_body)
        body = {"pool":_body}
        url = prefix + self.pool_path
        return self.base_update(obj_info = {'pool' : pool},
                                resource_url = url,
                                body = body,
                                **kwargs)

    def delete_pool(self, pool, prefix = '', **kwargs):
        """Deletes the specified load balancer pool.

        :param pool: ID of the pool.
        """
        url = prefix + self.pool_path
        return self.base_delete(obj_info = {'pool' : pool},
                                resource_url = url,
                                **kwargs)

    def retrieve_pool_stats(self, pool, prefix = '', params = None, **kwargs):
        """Retrieves stats for a certain load balancer pool.

        :param pool: ID of the pool.
        """
        url = prefix + self.pool_path_stats
        return self.base_show(obj_info = {'pool' : pool},
                             resource_url = url,
                             params = params,
                             **kwargs)
