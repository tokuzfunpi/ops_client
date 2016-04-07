from ops_client.manager.lbaas import LBaaSBaseManager

class HealthMonitorManager(LBaaSBaseManager):

    def list_health_monitors(self, prefix = '', params = None, **kwargs):
        """Fetches a list of all load balancer health monitors for a tenant."""
        # Pass filters in "params" argument to do_request
        url = prefix + self.health_monitors_path
        return self.base_list(resource_url = url,
                              params = params,
                              **kwargs)

    def show_health_monitor(self, health_monitor,
                            prefix = '', params = None, **kwargs):
        """Fetches information of a certain load balancer health monitor.

        :param health_monitor: ID of the health monitor.
        """
        url = prefix + self.health_monitor_path
        return self.base_show(
            obj_info = {'health_monitor' : health_monitor},
            resource_url = url,
            params = params,
            **kwargs)

    def create_health_monitor(self, hm_type, prefix = '',
                              max_retries = 3, delay = 180,
                              timeout = 60, hm_body = None, **kwargs):
        """Creates a new load balancer health monitor.

        :param type: monitor type. ex. 'PING', 'TCP', 'HTTP', 'HTTPS'
        :param max_retries: max retry times. default = 3.
        :param delay: delay time. default = 180.
        :param timeout: timeout. default = 60.
        """
        _body = {
            "type":hm_type,
            "max_retries":max_retries,
            "delay":delay,
            "timeout":timeout
        }
        if hm_body and type(hm_body) == dict :
            _body.update(hm_body)
        body = {"health_monitor":_body}
        url = prefix + self.health_monitors_path
        return self.base_create(resource_url = url,
                                body = body,
                                **kwargs)

    def update_health_monitor(self, health_monitor,
                              prefix = '', hm_body = None, **kwargs):
        """Updates a load balancer health monitor.

        :param health_monitor: ID of the health monitor.
        """
        _body = {}
        if hm_body and type(hm_body) == dict :
            _body.update(hm_body)
        body = {"health_monitor":_body}
        url = prefix + self.health_monitor_path
        return self.base_update(obj_info = {'health_monitor' : health_monitor},
                                resource_url = url,
                                body = body,
                                **kwargs)

    def delete_health_monitor(self, health_monitor, prefix = '', **kwargs):
        """Deletes the specified load balancer health monitor.

        :param health_monitor: ID of the health monitor.
        """
        url = prefix + self.health_monitor_path
        return self.base_delete(obj_info = {'health_monitor' : health_monitor},
                                resource_url = url,
                                **kwargs)

    def associate_health_monitor(self, health_monitor, pool,
                                 prefix = '', **kwargs):
        """Associate  specified load balancer health monitor and pool.

        :param health_monitor: ID of the health monitor.
        :param pool: ID of the pool.
        """
        body = {
            "health_monitor":{
                "id":health_monitor
            }
        }
        url = prefix + self.associate_pool_health_monitors_path
        return self.base_create(
            obj_info = {'pool' : pool},
            resource_url = url,
            body = body,
            **kwargs)

    def disassociate_health_monitor(self, pool, health_monitor,
                                    prefix = '', **kwargs):
        """Disassociate specified load balancer health monitor and pool.

        :param health_monitor: ID of the health monitor.
        :param pool: ID of the pool.
        """
        url = prefix + self.disassociate_pool_health_monitors_path
        return self.base_delete(
            obj_info = {'pool' : pool, 'health_monitor' : health_monitor},
            resource_url = url,
            **kwargs)
