from ops_client.manager.lbaas import LBaaSBaseManager

class VIPManager(LBaaSBaseManager):

    def list_vips(self, prefix = '', params = None, **kwargs):
        """Fetches a list of all load balancer vips for a tenant."""
        # Pass filters in "params" argument to do_request
        url = prefix + self.vips_path
        return self.base_list(resource_url = url,
                              params = params,
                              **kwargs)

    def show_vip(self, vip, prefix = '', params = None, **kwargs):
        """Fetches information of a certain load balancer vip.

        :param vip: ID of the vip.
        """
        url = prefix + self.vip_path
        return self.base_show(obj_info = {"vip" : vip},
                              resource_url = url,
                              params = params,
                              **kwargs)

    def create_vip(self, subnet, pool, protocol, protocol_port,
                   prefix = '', vip_body = None, **kwargs):
        """Creates a new load balancer vip.

        :param subnet: ID of the subnet.
        :param pool: ID of the pool.
        :param protocol: 'TCP','HTTP','HTTPS'
        :param protocol_port: port number.
        :param kwargs: vip values.
        """
        _body = {
            "subnet_id":subnet,
            "pool_id":pool,
            "protocol":protocol,
            "protocol_port":protocol_port
        }
        if vip_body and type(vip_body) == dict :
            _body.update(vip_body)
        body = {"vip":_body}
        url = prefix + self.vips_path
        return self.base_create(body = body,
                                resource_url = url,
                                **kwargs)

    def update_vip(self, vip, prefix = '', vip_body = None, **kwargs):
        """Updates a load balancer vip.

        :param vip: ID of the vip.
        :param kwargs: update values
        """
        _body = {}
        if vip_body and type(vip_body) == dict :
            _body.update(vip_body)
        body = {"vip":_body}
        url = prefix + self.vip_path
        return self.base_update(obj_info = {"vip" : vip},
                                resource_url = url,
                                body = body,
                                **kwargs)

    def delete_vip(self, vip, prefix = '', **kwargs):
        """Deletes the specified load balancer vip.

        :param vip: ID of the vip.
        """
        url = prefix + self.vip_path
        return self.base_delete(obj_info = {"vip" : vip},
                                resource_url = url,
                                **kwargs)
