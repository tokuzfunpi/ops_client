from ops_client.manager.neutron import NeutronBaseManager

class PortManager(NeutronBaseManager):

    def list_ports(self, params = None, **kwargs):
        """List ports that belong to a given tenant."""
        return self._get(self.ports_path, params = params, **kwargs)

    def show_port(self, port, params = None, **kwargs):
        """Fetches information of a certain network.

        :param port: ID of the port.
        """
        return self._get(self.port_path % (port), params = params, **kwargs)

    def create_port(self, network_id, port_body = None, **kwargs):
        """Create a port for a given tenant.

        :param network_id: ID of the network.
        """
        _body = {
            "network_id":network_id
        }
        if port_body and type(port_body) == dict :
            _body.update(port_body)
        body = {"port":_body}
        return self._post(self.ports_path, body = body, **kwargs)

    def update_port(self, port_id, port_body, **kwargs):
        """Update port's information.

        :param port: ID of the port.
        :param kwargs: update values.
        """
        body = {
            "port" : port_body
        }
        return self._put(self.port_path % (port_id), body = body, **kwargs)

    def delete_port(self, port_id, **kwargs):
        """Deletes the specified port.

        :param port: ID of the port.
        """
        return self._delete(self.port_path % (port_id), **kwargs)
