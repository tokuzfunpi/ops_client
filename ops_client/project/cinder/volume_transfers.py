from ops_client.manager.cinder import CinderBaseManager

class VolumeTransferManager(CinderBaseManager):
    def create(self, volume_id, name=None, **kwargs):
        """Creates a volume transfer.

        :param volume_id: The ID of the volume to transfer.
        :param name: The name of the transfer.
        :rtype: :class:`VolumeTransfer`
        """
        body = {'transfer': {'volume_id': volume_id,
                             'name': name}}
        return self._post('/os-volume-transfer', body = body, **kwargs)

    def accept(self, transfer_id, auth_key, **kwargs):
        """Accept a volume transfer.

        :param transfer_id: The ID of the transfer to accept.
        :param auth_key: The auth_key of the transfer.
        :rtype: :class:`VolumeTransfer`
        """
        body = {'accept': {'auth_key': auth_key}}
        return self._post('/os-volume-transfer/%s/accept' % transfer_id,
                            body = body, **kwargs)

    def get(self, transfer_id, **kwargs):
        """Show details of a volume transfer.

        :param transfer_id: The ID of the volume transfer to display.
        :rtype: :class:`VolumeTransfer`
        """
        return self._get("/os-volume-transfer/%s" % transfer_id, **kwargs)

    def list(self, detailed=True, search_opts=None, **kwargs):
        """Get a list of all volume transfer.

        :rtype: list of :class:`VolumeTransfer`
        """
        if detailed is True:
            return self._get("/os-volume-transfer/detail", **kwargs)
        else:
            return self._get("/os-volume-transfer", **kwargs)

    def delete(self, transfer_id, **kwargs):
        """Delete a volume transfer.

        :param transfer_id: The :class:`VolumeTransfer` to delete.
        """
        return self._delete("/os-volume-transfer/%s" % transfer_id, **kwargs)
