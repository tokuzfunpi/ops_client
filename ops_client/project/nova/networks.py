"""
Network interface. (For nova-network)
"""
from ops_client.common.exception import CommandError
from ops_client.manager.nova import NovaBaseManager

class NetworkManager(NovaBaseManager):

    def list(self, response_key = True, **kwargs):
        """
        Get a list of all networks.

        :rtype: list of :class:`Network`.
        """
        key = None
        if response_key :
            key = "networks"
        return self._get("/os-networks", key, **kwargs)

    def get(self, network_id, response_key = True, **kwargs):
        """
        Get a specific network.

        :param network: The ID of the :class:`Network` to get.
        :rtype: :class:`Network`
        """
        key = None
        if response_key :
            key = "network"
        return self._get("/os-networks/%s" % network_id, key, **kwargs)

    def delete(self, network_id, **kwargs):
        """
        Delete a specific network.

        :param network: The ID of the :class:`Network` to delete.
        """
        self._delete("/os-networks/%s" % network_id, **kwargs)

    def create(self, network_body, response_key = True, **kwargs):
        """
        Create (allocate) a network. The following parameters are
        optional except for label; cidr or cidr_v6 must be specified, too.

        :param label: str
        :param bridge: str
        :param bridge_interface: str
        :param cidr: str
        :param cidr_v6: str
        :param dns1: str
        :param dns2: str
        :param fixed_cidr: str
        :param gateway: str
        :param gateway_v6: str
        :param multi_host: str
        :param priority: str
        :param project_id: str
        :param vlan: int
        :param vlan_start: int
        :param vpn_start: int

        :rtype: list of :class:`Network`
        """
        body = {"network": network_body}
        key = None
        if response_key :
            key = "network"
        return self._post('/os-networks', body, key, **kwargs)

    def disassociate(self, network_id, disassociate_host = True,
                     disassociate_project = True, **kwargs):
        """
        Disassociate a specific network from project and/or host.

        :param network: The ID of the :class:`Network`.
        :param disassociate_host: Whether to disassociate the host
        :param disassociate_project: Whether to disassociate the project
        """
        if disassociate_host and disassociate_project:
            body = {"disassociate": None}
        elif disassociate_project:
            body = {"disassociate_project": None}
        elif disassociate_host:
            body = {"disassociate_host": None}
        else:
            raise CommandError(
                "Must disassociate either host or project or both")

        self._post("/os-networks/%s/action" %
                             network_id, body=body, **kwargs)

    def associate_host(self, network_id, host, **kwargs):
        """
        Associate a specific network with a host.

        :param network: The ID of the :class:`Network`.
        :param host: The name of the host to associate the network with
        """
        self._post("/os-networks/%s/action" %
                             network_id,
                             body={"associate_host": host}, **kwargs)

    def associate_project(self, network_id, **kwargs):
        """
        Associate a specific network with a project.

        The project is defined by the project authenticated against

        :param network: The ID of the :class:`Network`.
        """
        self._post("/os-networks/add", body={"id": network_id}, **kwargs)

    def add(self, network_id=None, **kwargs):
        """
        Associates the current project with a network. Network can be chosen
        automatically or provided explicitly.

        :param network: The ID of the :class:`Network` to associate (optional).
        """
        self._post(
            "/os-networks/add",
            body={"id": network_id if network_id else None}, **kwargs)
