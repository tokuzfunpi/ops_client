from ops_client.manager.neutron import NeutronBaseManager

class NetworkManager(NeutronBaseManager):

    def list_networks(self, params = None, **kwargs):
        """Fetches a list of all networks for a tenant."""
        # Pass filters in "params" argument to do_request
        return self._get(self.networks_path , params=params, **kwargs)

    def show_network(self, network, params = None, **kwargs):
        """Fetches information of a certain network.

        :param network: ID of the network.
        """
        return self._get(self.network_path % (network), params=params, **kwargs)

    def create_network(self, network_body, **kwargs):
        """Creates a new network.

        :param network_body: network values.
        """
        body = {
            "network" : network_body
        }
        return self._post(self.networks_path, body=body, **kwargs)

    def update_network(self, network_id, network_body, **kwargs):
        """Updates a network.

        :param network_id: ID of the network.
        """
        body = {
            "network" : network_body
        }
        return self._put(self.network_path % (network_id), body=body, **kwargs)

    def delete_network(self, network_id, **kwargs):
        """Deletes the specified network.

        :params network_id: ID of the network.
        """
        return self._delete(self.network_path % (network_id), **kwargs)
