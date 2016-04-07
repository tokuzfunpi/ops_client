from ops_client.manager.lbaas import LBaaSBaseManager

class MemberManager(LBaaSBaseManager):

    def list_members(self, prefix = '', params = None, **kwargs):
        """Fetches a list of all load balancer members for a tenant."""
        # Pass filters in "params" argument to do_request
        url = prefix + self.members_path
        return self.base_list(resource_url = url,
                              params = params,
                              **kwargs)

    def show_member(self, member, prefix = '', params = None, **kwargs):
        """Fetches information of a certain load balancer member.

        :param member: ID of the member.
        """
        url = prefix + self.member_path
        return self.base_show(obj_info = {'member' : member},
                              resource_url = url,
                              params = params,
                              **kwargs)

    def create_member(self, pool_id, address, protocol_port, 
                      prefix = '', member_body = None, **kwargs):
        """Creates a new load balancer member.

        :param pool_id: ID of the pool.
        :param address: IP address.
        :param protocol_port: Port number.
        :param kwargs: other values.
        """
        _body = {
            "pool_id":pool_id,
            "address":address,
            "protocol_port":protocol_port
        }
        if member_body and type(member_body) == dict :
            _body.update(member_body)
        body = {"member":_body}
        url = prefix + self.members_path
        return self.base_create(resource_url = url,
                                body = body,
                                **kwargs)

    def update_member(self, member, prefix = '', member_body = None, **kwargs):
        """Updates a load balancer member.

        :param member: ID of the member.
        :param kwargs: update values.
        """
        _body = {}
        if member_body and type(member_body) == dict :
            _body.update(member_body)
        body = {"member":_body}
        url = prefix + self.member_path
        return self.base_update(obj_info = {'member' : member},
                                resource_url = url,
                                body = body,
                                **kwargs)

    def delete_member(self, member, prefix = '', **kwargs):
        """Deletes the specified load balancer member.

        :param member: ID of the member.
        """
        url = prefix + self.member_path
        return self.base_delete(obj_info = {'member' : member},
                                resource_url = url,
                                **kwargs)
