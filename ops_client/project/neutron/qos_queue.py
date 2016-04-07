from ops_client.manager.neutron import NeutronBaseManager

class QosQueueManager(NeutronBaseManager):
    """
    .. warning::

       return 404.
    """

    def create_qos_queue(self, body=None):
        """Creates a new queue."""
        return self._post(self.qos_queues_path, body=body)

    def list_qos_queues(self, params = None):
        """Fetches a list of all queues for a tenant."""
        return self._get(self.qos_queues_path, params=params)

    def show_qos_queue(self, queue, params = None):
        """Fetches information of a certain queue."""
        return self._get(self.qos_queue_path % (queue),
                        params=params)

    def delete_qos_queue(self, queue):
        """Deletes the specified queue."""
        return self._delete(self.qos_queue_path % (queue))
