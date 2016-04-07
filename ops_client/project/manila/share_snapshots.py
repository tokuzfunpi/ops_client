from ops_client.manager.manila import ManilaBaseManager
from ops_client.common import manila_constants as constants
try:
    from urllib import urlencode  # noqa
except ImportError:
    from urllib.parse import urlencode  # noqa


class ShareSnapshotManager(ManilaBaseManager):
    """Manage :class:`ShareSnapshot` resources."""

    def create(self, share_id, force=False, name=None, description=None,
               **kwargs):
        """Create a snapshot of the given share.

        :param share_id: The ID of the share to snapshot.
        :param force: If force is True, create a snapshot even if the
                      share is busy. Default is False.
        :param name: Name of the snapshot
        :param description: Description of the snapshot
        :rtype: :class:`ShareSnapshot`
        """
        body = {
            'snapshot': {
                'share_id': share_id,
                'force': force,
                'name': name,
                'description': description
            }
        }
        print 'create_body',body
        return self._post('/snapshots', body=body, **kwargs)

    def get(self, snapshot_id, **kwargs):
        """Get a snapshot.

        :param snapshot: The :class:`ShareSnapshot` instance or string with ID
            of snapshot to delete.
        :rtype: :class:`ShareSnapshot`
        """
        return self._get('/snapshots/%s' % snapshot_id, **kwargs)

    def list(self, detailed=True, search_opts=None, sort_key=None,
             sort_dir=None, **kwargs):
        """Get a list of snapshots of shares.

        :param search_opts: Search options to filter out shares.
        :param sort_key: Key to be sorted.
        :param sort_dir: Sort direction, should be 'desc' or 'asc'.
        :rtype: list of :class:`ShareSnapshot`
        """
        if search_opts is None:
            search_opts = {}

        if sort_key is not None:
            if sort_key in constants.SNAPSHOT_SORT_KEY_VALUES:
                search_opts['sort_key'] = sort_key
            else:
                raise ValueError(
                    'sort_key must be one of the following: %s.'
                    % ', '.join(constants.SNAPSHOT_SORT_KEY_VALUES))

        if sort_dir is not None:
            if sort_dir in constants.SORT_DIR_VALUES:
                search_opts['sort_dir'] = sort_dir
            else:
                raise ValueError(
                    'sort_dir must be one of the following: %s.'
                    % ', '.join(constants.SORT_DIR_VALUES))

        if search_opts:
            query_string = urlencode(
                sorted([(k, v) for (k, v) in list(search_opts.items()) if v]))
            if query_string:
                query_string = "?%s" % (query_string,)
        else:
            query_string = ''

        if detailed:
            path = "/snapshots/detail%s" % (query_string,)
        else:
            path = "/snapshots%s" % (query_string,)

        return self._get(path, **kwargs)

    def delete(self, snapshot_id, **kwargs):
        """Delete a snapshot of a share.

        :param snapshot: The :class:`ShareSnapshot` to delete.
        """
        return self._delete("/snapshots/%s" % snapshot_id, **kwargs)

    def force_delete(self, snapshot):
        return self._action('os-force_delete', common_base.getid(snapshot))

    def update(self, snapshot_id, updates=None, **kwargs):
        """Update a snapshot.

        :param snapshot: The :class:`ShareSnapshot` instance or string with ID
            of snapshot to delete.
        :rtype: :class:`ShareSnapshot`
        """
        if not updates:
            return

        body = {'snapshot': updates}
        return self._put("/snapshots/%s" % snapshot_id, body, **kwargs)

    def reset_state(self, snapshot, state):
        """Update the specified share snapshot with the provided state."""
        return self._action('os-reset_status', snapshot, {'status': state})

    def _action(self, action, snapshot, info=None, **kwargs):
        """Perform a  snapshot 'action'."""
        body = {action: info}
        self.run_hooks('modify_body_for_action', body, **kwargs)
        url = '/snapshots/%s/action' % common_base.getid(snapshot)
        return self.api.client.post(url, body=body)
