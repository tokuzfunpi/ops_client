"""
Volume snapshot interface.

.. warning::
   Please use cinder-client volume snapshot lib instead of use this lib.
"""

from ops_client.manager.nova import NovaBaseManager

class SnapshotManager(NovaBaseManager):

    def create(self, volume_id, force=False,
                    display_name=None, display_description=None,
                    response_key = True, **kwargs):
        """
        Create a snapshot of the given volume.

        :param volume_id: The ID of the volume to snapshot.
        :param force: If force is True, create a snapshot even if the volume is
        attached to an instance. Default is False.
        :param display_name: Name of the snapshot
        :param display_description: Description of the snapshot
        :rtype: :class:`Snapshot`
        """
        body = {'snapshot': {'volume_id': volume_id,
                            'force': force,
                            'display_name': display_name,
                            'display_description': display_description}}
        if response_key :
            return self._post('/snapshots', body, 'snapshot', **kwargs)
        else :
            return self._post('/snapshots', body, **kwargs)

    def get(self, snapshot_id, response_key = True, **kwargs):
        """
        Get a snapshot.

        :param snapshot_id: The ID of the snapshot to get.
        :rtype: :class:`Snapshot`
        """
        if response_key :
            return self._get("/snapshots/%s" % snapshot_id, "snapshot", 
                             **kwargs)
        else:
            return self._get("/snapshots/%s" % snapshot_id, **kwargs)

    def list(self, detailed=True, response_key = True, **kwargs):
        """
        Get a list of all snapshots.

        :rtype: list of :class:`Snapshot`
        """
        if detailed is True:
            if response_key :
                return self._get("/snapshots/detail", "snapshots", **kwargs)
            else :
                return self._get("/snapshots/detail", **kwargs)
        else:
            if response_key :
                return self._get("/snapshots", "snapshots", **kwargs)
            else :
                return self._get("/snapshots", **kwargs)

    def delete(self, snapshot_id, **kwargs):
        """
        Delete a snapshot.

        :param snapshot: The :class:`Snapshot` to delete.
        """
        return self._delete("/snapshots/%s" % snapshot_id, **kwargs)
