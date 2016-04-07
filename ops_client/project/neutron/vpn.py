from ops_client.manager.neutron import NeutronBaseManager

class VPNManager(NeutronBaseManager):

    def list_vpnservices(self, params = None):
        """Fetches a list of all configured VPN services for a tenant."""
        return self._get(self.vpnservices_path, params=params)

    def show_vpnservice(self, vpnservice, params = None):
        """Fetches information of a specific VPN service.

        :param vpnservice: ID of the VPN service
        """
        return self._get(self.vpnservice_path % (vpnservice), params=params)

    def create_vpnservice(self, router_id, subnet_id,
                          vpn_body = None, **kwargs):
        """Creates a new VPN service.

        :param router_id: ID of the router.
        :param subnet_id: ID of the subnet.
        :param kwargs: VPN service values.
        """
        _body = {
            "router_id":router_id,
            "subnet_id":subnet_id
        }
        if vpn_body and type(vpn_body) == dict :
            _body.update(vpn_body)
        body = {"vpnservice":_body}
        return self._post(self.vpnservices_path, body=body)

    def update_vpnservice(self, vpnservice, vpn_body = None, **kwargs):
        """Updates a VPN service.

        :param vpnservice: ID of the VPN service
        """
        _body = {}
        if vpn_body and type(vpn_body) == dict :
            _body.update(vpn_body)
        body = {"vpnservice":_body}
        return self._put(self.vpnservice_path % (vpnservice), body=body)

    def delete_vpnservice(self, vpnservice):
        """Deletes the specified VPN service.

        :param vpnservice: ID of the VPN service
        """
        return self._delete(self.vpnservice_path % (vpnservice))
