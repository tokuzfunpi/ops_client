import six
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
from ops_client.manager.cinder import CinderBaseManager

class SnapshotManager(CinderBaseManager):

    def create(self, volume_id, force=False, name=None, description=None, 
               **kwargs):
        """Creates a snapshot of the given volume.

        :param volume_id: The ID of the volume to snapshot.
        :param force: If force is True, create a snapshot even if the volume is
        attached to an instance. Default is False.
        :param name: Name of the snapshot
        :param description: Description of the snapshot
        :rtype: :class:`Snapshot`
        """
        body = {'snapshot': {'volume_id': volume_id,
                             'force': force,
                             'name': name,
                             'description': description}}
        return self._post('/snapshots', body = body, **kwargs)

    def get(self, snapshot_id, **kwargs):
        """Shows snapshot details.

        :param snapshot_id: The ID of the snapshot to get.
        :rtype: :class:`Snapshot`
        """
        return self._get("/snapshots/%s" % snapshot_id, **kwargs)

    def list(self, detailed=True, search_opts=None, **kwargs):
        """Get a list of all snapshots.

        :rtype: list of :class:`Snapshot`
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in six.iteritems(search_opts):
            if val:
                qparams[opt] = val

        # Transform the dict to a sequence of two-element tuples in fixed
        # order, then the encoded string will be consistent in Python 2&3.
        if qparams:
            new_qparams = sorted(qparams.items(), key=lambda x: x[0])
            query_string = "?%s" % urlencode(new_qparams)
        else:
            query_string = ""

        detail = ""
        if detailed:
            detail = "/detail"

        return self._get("/snapshots%s%s" % (detail, query_string), **kwargs)

    def delete(self, snapshot_id, **kwargs):
        """Delete a snapshot.

        :param snapshot_id: The :class:`Snapshot` to delete.
        """
        return self._delete("/snapshots/%s" % snapshot_id, **kwargs)

    def update(self, snapshot_id, updates = None, **kwargs):
        """Update the name or description for a snapshot.

        :param snapshot_id: The :class:`Snapshot` to update.
        """
        if not updates:
            return

        body = {"snapshot": updates}

        return self._put("/snapshots/%s" % snapshot_id, body, **kwargs)

    def reset_state(self, snapshot_id, state, **kwargs):
        """Update the specified snapshot with the provided state.

        :param snapshot_id: ID of the snapshot.
        :param state: snapshot state.
        """
        return self._action('os-reset_status', snapshot_id, 
                            {'status': state}, **kwargs)

    def _action(self, action, snapshot_id, info=None, 
                raw_body = None, **kwargs):
        """Perform a snapshot action."""
        if not raw_body :
            body = {action: info}
        else :
            body = raw_body
        url = '/snapshots/%s/action' % snapshot_id
        return self._post(url, body=body, **kwargs)

    def update_snapshot_status(self, snapshot_id, update_dict, **kwargs):
        return self._action('os-update_snapshot_status',
                            snapshot_id, update_dict, **kwargs)

    def set_metadata(self, snapshot_id, metadata, **kwargs):
        """Update/Set a snapshots metadata.

        :param snapshot_id: The :class:`Snapshot`.
        :param metadata: A list of keys to be set.
        """
        body = {'metadata': metadata}
        return self._post("/snapshots/%s/metadata" % snapshot_id,
                            body, **kwargs)

    def delete_metadata(self, snapshot_id, key, **kwargs):
        """Delete specified keys from snapshot metadata.

        :param snapshot_id: The :class:`Snapshot`.
        :param key: A string of key to be removed.
        """
        return self._delete("/snapshots/%s/metadata/%s" % (snapshot_id, key),
                            **kwargs)

    def update_all_metadata(self, snapshot_id, metadata, **kwargs):
        """Update_all snapshot metadata.

        :param snapshot_id: The :class:`Snapshot`.
        :param metadata: A list of keys to be updated.
        """
        body = {'metadata': metadata}
        return self._put("/snapshots/%s/metadata" % snapshot_id, body = body, 
                         **kwargs)
