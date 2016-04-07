from ops_client.manager.neutron import NeutronBaseManager

class NetPartitionManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    def list_net_partitions(self, params = None):
        """Fetch a list of all network partitions for a tenant."""
        return self._get(self.net_partitions_path, params=params)

    def show_net_partition(self, netpartition, params = None):
        """Fetch a network partition."""
        return self._get(self.net_partition_path % (netpartition),
                        params=params)

    def create_net_partition(self, body=None):
        """Create a network partition."""
        return self._post(self.net_partitions_path, body=body)

    def delete_net_partition(self, netpartition):
        """Delete the network partition."""
        return self._delete(self.net_partition_path % netpartition)
