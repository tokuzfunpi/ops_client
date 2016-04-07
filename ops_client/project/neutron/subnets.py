from ops_client.manager.neutron import NeutronBaseManager

class SubnetManager(NeutronBaseManager):

    def list_subnets(self, params = None, **kwargs):
        """Fetches a list of all networks for a tenant."""
        return self._get(self.subnets_path, params = params, **kwargs)

    def show_subnet(self, subnet_id, params = None, **kwargs):
        """Fetches information of a certain subnet.

        :param subnet: ID of the subnet.
        """
        return self._get(self.subnet_path % (subnet_id), params=params, 
                         **kwargs)

    def create_subnet(self, network_id, ip_version, cidr, 
                      subnet_body = None, **kwargs):
        """Creates a new subnet.

        :param network_id: ID of the network.
        :param ip_version: 4 or 6 (int)
        :param cidr: cidr of the subnet.
        """
        _body = {
            "ip_version" : ip_version,
            "network_id" : network_id,
            "cidr" : cidr
        }
        if subnet_body and type(subnet_body) == dict :
            _body.update(subnet_body)
        body = {"subnet":_body}
        return self._post(self.subnets_path, body=body, **kwargs)

    def update_subnet(self, subnet_id, subnet_body, **kwargs):
        """Updates a subnet.

        :param subnet: ID of the subnet.
        :param kwargs: update values.
        """
        body = {
            "subnet" : subnet_body
        }
        return self._put(self.subnet_path % (subnet_id), body=body, **kwargs)

    def delete_subnet(self, subnet, **kwargs):
        """Deletes the specified subnet.

        :param subnet: ID of the subnet.
        """
        return self._delete(self.subnet_path % (subnet), **kwargs)
