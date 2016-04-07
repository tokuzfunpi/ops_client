from ops_client.manager.neutron import NeutronBaseManager

class PacketFilterManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    def create_packet_filter(self, body=None):
        """Create a new packet filter."""
        return self._post(self.packet_filters_path, body=body)

    def update_packet_filter(self, packet_filter_id, body=None):
        """Update a packet filter."""
        return self._put(self.packet_filter_path % packet_filter_id, body=body)

    def list_packet_filters(self, params = None):
        """Fetch a list of all packet filters for a tenant."""
        return self._get(self.packet_filters_path, params=params)

    def show_packet_filter(self, packet_filter_id, params = None):
        """Fetch information of a certain packet filter."""
        return self._get(self.packet_filter_path % packet_filter_id,
                        params=params)

    def delete_packet_filter(self, packet_filter_id):
        """Delete the specified packet filter."""
        return self._delete(self.packet_filter_path % packet_filter_id)
