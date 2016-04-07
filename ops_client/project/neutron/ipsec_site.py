from ops_client.manager.neutron import NeutronBaseManager

class IpsecSiteManager(NeutronBaseManager):
    """
    .. warning::

       Make sure you had created IPsecPolicy, IKEPolicy and VPNservice 
       before you create IPsecSiteConnection.
    """

    def list_ipsec_site_connections(self, params = None):
        """Fetches all configured IPsecSiteConnections for a tenant."""
        return self._get(self.ipsec_site_connections_path, params=params)

    def show_ipsec_site_connection(self, ipsecsite_conn, params = None):
        """Fetches information of a specific IPsecSiteConnection.

        :param ipsecsite_conn: ID of the IPsecSiteConnection.
        """
        return self._get(
            self.ipsec_site_connection_path % (ipsecsite_conn), 
            params=params)

    def create_ipsec_site_connection(self,ipsecpolicy_id, ikepolicy_id,
                                     vpnservice_id, psk, peer_cidrs,
                                     peer_address, peer_id,
                                     ipsec_body = None, **kwargs):
        """Creates a new IPsecSiteConnection.

        :param ipsecpolicy_id: ID of the IPsecPolicy.
        :param ikepolicy_id: ID of the ikepolicy.
        :param vpnservice_id: ID of the VPN service.
        :param psk: (string)
        :param peer_cidrs: cidr of the peer.
        :param peer address: address of the peer.
        :param peer_id: ID of the peer.
        :param kwargs: other values.
        """
        _body = {
            "psk":psk,
            "peer_cidrs":peer_cidrs,
            "ipsecpolicy_id":ipsecpolicy_id,
            "ikepolicy_id":ikepolicy_id,
            "vpnservice_id":vpnservice_id,
            "peer_address":peer_address,
            "peer_id":peer_id
        }
        if ipsec_body and type(ipsec_body) == dict :
            _body.update(ipsec_body)
        body = {"ipsec_site_connection":_body}
        return self._post(self.ipsec_site_connections_path, body=body)

    def update_ipsec_site_connection(self, ipsecsite_conn,
                                     ipsec_body = None, **kwargs):
        """Updates an IPsecSiteConnection.

        :param ipsecsite_conn: ID of the IPsecSiteConnection.
        :param kwargs: update values
        """
        _body = {}
        if ipsec_body and type(ipsec_body) == dict :
            _body.update(ipsec_body)
        body = {"ipsec_site_connection":_body}
        return self._put(
            self.ipsec_site_connection_path % (ipsecsite_conn), body=body
        )

    def delete_ipsec_site_connection(self, ipsecsite_conn):
        """Deletes the specified IPsecSiteConnection.

        :param ipsecsite_conn: ID of the IPsecSiteConnection.
        """
        return self._delete(self.ipsec_site_connection_path % (ipsecsite_conn))
