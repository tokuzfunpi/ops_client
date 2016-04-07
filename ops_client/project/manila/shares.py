from ops_client.manager.manila import ManilaBaseManager
from ops_client.common import manila_constants as constants

import collections
# import re
try:
    from urllib import urlencode  # noqa
except ImportError:
    from urllib.parse import urlencode  # noqa


class ShareManager(ManilaBaseManager):
    """Manage :class:`Share` resources."""

    def create(self, share_proto, size, snapshot_id=None, name=None,
               description=None, metadata=None, share_network_id=None,
               share_type_id=None, is_public=False, availability_zone=None,
               consistency_group_id=None, **kwargs):
        """Create a share.

        :param share_proto: text - share protocol for new share
            available values are NFS, CIFS, GlusterFS and HDFS.
        :param size: int - size in GB
        :param snapshot_id: text - ID of the snapshot
        :param name: text - name of new share
        :param description: text - description of a share
        :param metadata: dict - optional metadata to set on share creation
        :param share_network: either instance of ShareNetwork or text with ID
        :param share_type: either instance of ShareType or text with ID
        :param is_public: bool, whether to set share as public or not.
        :param consistency_group_id: text - ID of the consistency group to
            which the share should belong
        :rtype: :class:`Share`
        """
        share_metadata = metadata if metadata is not None else dict()
        body = {
            'size': size,
            'snapshot_id': snapshot_id,
            'name': name,
            'description': description,
            'metadata': share_metadata,
            'share_proto': share_proto,
            'share_network_id': share_network_id,
            'share_type': share_type_id,
            'is_public': is_public,
            'availability_zone': availability_zone,
            'consistency_group_id': consistency_group_id,
        }
        return self._post('/shares', body={'share': body}, **kwargs)

    def migrate_share(self, share, host, force_host_copy):
        """Migrate share to new host and pool.

        :param share: The :class:'share' to migrate
        :param host: The destination host and pool
        :param force_host_copy: Skip driver optimizations
        """
        # return self._action('os-migrate_share',
        #                     share, {'host': host,
        #                             'force_host_copy': force_host_copy})
        pass  # v2.5

    # def manage(self, service_host, protocol, export_path,
    #            driver_options=None, share_type=None,
    #            name=None, description=None):
    #     """Manage some existing share.

    #     :param service_host: text - host of share service where share is runing
    #     :param protocol: text - share protocol that is used
    #     :param export_path: text - export path of share
    #     :param driver_options: dict - custom set of key-values.
    #     :param share_type: text - share type that should be used for share
    #     :param name: text - name of new share
    #     :param description: - description for new share
    #     """
    #     driver_options = driver_options if driver_options else dict()
    #     body = {
    #         'service_host': service_host,
    #         'share_type': share_type,
    #         'protocol': protocol,
    #         'export_path': export_path,
    #         'driver_options': driver_options,
    #         'name': name,
    #         'description': description
    #     }
    #     return self._create('/os-share-manage', {'share': body}, 'share')

    # def unmanage(self, share):
    #     """Unmanage a share.

    #     :param share: either share object or text with its ID.
    #     """
    #     return self.api.client.post(
    #         "/os-share-unmanage/%s/unmanage" % common_base.getid(share))

    def get(self, share_id, **kwargs):
        """Get a share.

        :param share: either share object or text with its ID.
        :rtype: :class:`Share`
        """
        return self._get("/shares/%s" % share_id, **kwargs)

    def update(self, share_id, updates=None, **kwargs):
        """Updates a share.

        :param share: either share object or text with its ID.
        :rtype: :class:`Share`
        """
        if not updates:
            return
        body = {'share': updates}
        return self._put("/shares/%s" % share_id, body, **kwargs)

    def list(self, detailed=True, search_opts=None,
             sort_key=None, sort_dir=None, **kwargs):
        """Get a list of all shares.

        :param detailed: Whether to return detailed share info or not.
        :param search_opts: dict with search options to filter out shares.
            available keys are below (('name1', 'name2', ...), 'type'):
            - ('all_tenants', int)
            - ('is_public', bool)
            - ('metadata', dict)
            - ('extra_specs', dict)
            - ('limit', int)
            - ('offset', int)
            - ('name', text)
            - ('status', text)
            - ('host', text)
            - ('share_server_id', text)
            - (('share_network_id', 'share_network'), text)
            - (('share_type_id', 'share_type'), text)
            - (('snapshot_id', 'snapshot'), text)
            Note, that member context will have restricted set of
            available search opts. For admin context filtering also available
            by each share attr from its Model. So, this list is not full for
            admin context.
        :param sort_key: Key to be sorted (i.e. 'created_at' or 'status').
        :param sort_dir: Sort direction, should be 'desc' or 'asc'.
        :rtype: list of :class:`Share`
        """
        if search_opts is None:
            search_opts = {}

        if sort_key is not None:
            if sort_key in constants.SHARE_SORT_KEY_VALUES:
                search_opts['sort_key'] = sort_key
                # NOTE(vponomaryov): Replace aliases with appropriate keys
                if sort_key == 'share_type':
                    search_opts['sort_key'] = 'share_type_id'
                elif sort_key == 'snapshot':
                    search_opts['sort_key'] = 'snapshot_id'
                elif sort_key == 'share_network':
                    search_opts['sort_key'] = 'share_network_id'
            else:
                raise ValueError('sort_key must be one of the following: %s.'
                                 % ', '.join(constants.SHARE_SORT_KEY_VALUES))

        if sort_dir is not None:
            if sort_dir in constants.SORT_DIR_VALUES:
                search_opts['sort_dir'] = sort_dir
            else:
                raise ValueError('sort_dir must be one of the following: %s.'
                                 % ', '.join(constants.SORT_DIR_VALUES))

        if 'is_public' not in search_opts:
            search_opts['is_public'] = True

        if search_opts:
            query_string = urlencode(
                sorted([(k, v) for (k, v) in list(search_opts.items()) if v]))
            if query_string:
                query_string = "?%s" % (query_string,)
        else:
            query_string = ''

        if detailed:
            path = "/shares/detail%s" % (query_string,)
        else:
            path = "/shares%s" % (query_string,)

        return self._get(path, **kwargs)

    def delete(self, share_id, consistency_group_id=None, **kwargs):
        """Delete a share.

        :param share: either share object or text with its ID.
        :param consistency_group_id: text - ID of the consistency group to
            which the share belongs to.
        """
        url = "/shares/%s" % share_id
        if consistency_group_id:
            url += "?consistency_group_id=%s" % consistency_group_id
        return self._delete(url, **kwargs)

    def force_delete(self, share_id, **kwargs):
        """Delete a share forcibly - share status will be avoided.

        :param share: either share object or text with its ID.
        """
        return self._action('os-force_delete', share_id, **kwargs)

    def allow(self, share_id, access_type, access_to, access_level, **kwargs):
        """Allow access to a share.

        :param share_id: share ID.
        :param access_type: string that represents access type ('ip','domain')
        :param access_to: string that represents access ('127.0.0.1')
        :param access_level: string that represents access level ('rw', 'ro')
        """
        access_params = {
            'access_type': access_type,
            'access_to': access_to,
        }
        if access_level:
            access_params['access_level'] = access_level
        return self._action('os-allow_access', share_id,
                            access_params, **kwargs)

    def deny(self, share_id, access_id, **kwargs):
        """Deny access to a share.

        :param share_id: share ID.
        :param access_id: ID of share access rule
        """
        deny_body = {'access_id': access_id}
        return self._action('os-deny_access', share_id, deny_body, **kwargs)

    def access_list(self, share_id, **kwargs):
        """Get access list to a share.

        :param share: share ID.
        """
        return self._action("os-access_list", share_id, **kwargs)

    def get_metadata(self, share_id, **kwargs):
        """Get metadata of a share.

        :param share: either share object or text with its ID.
        """
        return self._get("/shares/%s/metadata" % share_id,
                         **kwargs)

    def set_metadata(self, share_id, metadata, **kwargs):
        """Set or update metadata for share.

        :param share: either share object or text with its ID.
        :param metadata: A list of keys to be set.
        """
        body = {'metadata': metadata}
        return self._post("/shares/%s/metadata" % share_id,
                          body=body, **kwargs)

    def delete_metadata(self, share_id, key, **kwargs):
        """Delete specified keys from shares metadata.

        :param share: either share object or text with its ID.
        :param keys: A list of keys to be removed.
        """
        return self._delete("/shares/%(share_id)s/metadata/%(key)s" % {
            'share_id': share_id, 'key': key}, **kwargs)

    def update_all_metadata(self, share_id, metadata, **kwargs):
        """Update all metadata of a share.

        :param share: either share object or text with its ID.
        :param metadata: A list of keys to be updated.
        """
        body = {'metadata': metadata}
        return self._put("/shares/%s/metadata" % share_id, body, **kwargs)

    def _action(self, action, share_id, info=None, raw_body=None,
                resource_url="/shares/%s/action", **kwargs):
        """
        Perform a server "action" -- reboot/rebuild/resize/etc.
        """
        if not raw_body:
            body = {action: info}
        else:
            body = raw_body
        return self._post(resource_url % share_id, body, **kwargs)

    def reset_state(self, share_id, state, **kwargs):
        """Update the provided share with the provided state.

        :param share: either share object or text with its ID.
        :param state: text with new state to set for share.
        """
        return self._action('os-reset_status', share_id,
                            info={'status': state}, **kwargs)

    def extend(self, share_id, new_size, **kwargs):
        """Extend the size of the specified share.

        :param share: either share object or text with its ID.
        :param new_size: The desired size to extend share to.
        """
        return self._action('os-extend', share_id,
                            info={'new_size': new_size}, **kwargs)

    def shrink(self, share_id, new_size, **kwargs):
        """Shrink the size of the specified share.

        :param share: either share object or text with its ID.
        :param new_size: The desired size to shrink share to.
        """
        return self._action('os-shrink', share_id,
                            info={'new_size': new_size}, **kwargs)

    def list_instances(self, share_id, **kwargs):
        """List instances of the specified share.

        :param share: either share object or text with its ID.
        """
        # return self._list(
        #     '/shares/%s/instances' % common_base.getid(share),
        #     'share_instances',
        #     obj_class=share_instances.ShareInstance
        # )
        pass  # v2.3 support
