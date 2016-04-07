import six
from ops_client.manager.cinder import CinderBaseManager
from urllib import urlencode

class VolumeManager(CinderBaseManager):

    def create(self, size, snapshot_id=None, source_volid=None,
               name=None, description=None,
               volume_type=None, user_id=None,
               project_id=None, availability_zone=None,
               metadata=None, imageRef=None, scheduler_hints=None, **kwargs):
        """Creates a volume.

        :param size: Size of volume in GB
        :param snapshot_id: ID of the snapshot
        :param name: Name of the volume
        :param description: Description of the volume
        :param volume_type: Type of volume
        :param user_id: User id derived from context
        :param project_id: Project id derived from context
        :param availability_zone: Availability Zone to use
        :param metadata: Optional metadata to set on volume creation
        :param imageRef: reference to an image stored in glance
        :param source_volid: ID of source volume to clone from
        :param scheduler_hints: (optional extension) arbitrary key-value pairs
                            specified by the client to help boot an instance
        :rtype: :class:`Volume`
       """

        if metadata is None:
            volume_metadata = {}
        else:
            volume_metadata = metadata

        body = {'volume': {'size': size,
                           'snapshot_id': snapshot_id,
                           'name': name,
                           'description': description,
                           'volume_type': volume_type,
                           'user_id': user_id,
                           'project_id': project_id,
                           'availability_zone': availability_zone,
                           'status': "creating",
                           'attach_status': "detached",
                           'metadata': volume_metadata,
                           'imageRef': imageRef,
                           'source_volid': source_volid,
                           }}

        if scheduler_hints:
            body['OS-SCH-HNT:scheduler_hints'] = scheduler_hints

        return self._post('/volumes', body = body, **kwargs)

    def get(self, volume_id, **kwargs):
        """Get a volume.

        :param volume_id: The ID of the volume to get.
        :rtype: :class:`Volume`
        """
        return self._get("/volumes/%s" % volume_id, **kwargs)

    def list(self, detailed=True, search_opts=None, **kwargs):
        """Lists all volumes.

        :rtype: list of :class:`Volume`
        """
        if search_opts is None:
            search_opts = {}

        qparams = {}

        for opt, val in six.iteritems(search_opts):
            if val:
                qparams[opt] = val

        query_string = "?%s" % urlencode(qparams) if qparams else ""

        detail = ""
        if detailed:
            detail = "/detail"

        return self._get("/volumes%s%s" % (detail, query_string), **kwargs)

    def delete(self, volume_id, **kwargs):
        """Delete a volume.

        :param volume_id: The :class:`Volume` to delete.
        """
        return self._delete("/volumes/%s" % volume_id, **kwargs)

    def update(self, volume_id, updates = None, **kwargs):
        """Update the name or description for a volume.

        :param volume_id: The :class:`Volume` to update.
        """
        if not updates:
            return

        body = {"volume": updates}

        return self._put("/volumes/%s" % volume_id, body, **kwargs)

    def _action(self, action, volume_id, info=None, raw_body = None, **kwargs):
        """Perform a volume "action."
        """
        if not raw_body :
            body = {action: info}
        else :
            body = raw_body
        url = '/volumes/%s/action' % volume_id
        return self._post(url, body=body, **kwargs)

    def attach(self, volume_id, instance_uuid, mountpoint, mode='rw', **kwargs):
        """Set attachment metadata.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to attach.
        :param instance_uuid: uuid of the attaching instance.
        :param mountpoint: mountpoint on the attaching instance.
        :param mode: the access mode.
        """
        return self._action('os-attach',
                            volume_id,
                            {'instance_uuid': instance_uuid,
                             'mountpoint': mountpoint,
                             'mode': mode}, **kwargs)

    def detach(self, volume_id, **kwargs):
        """Clear attachment metadata.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to detach.
        """
        return self._action('os-detach', volume_id, **kwargs)

    def reserve(self, volume_id, **kwargs):
        """Reserve this volume.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to reserve.
        """
        return self._action('os-reserve', volume_id, **kwargs)

    def unreserve(self, volume_id, **kwargs):
        """Unreserve this volume.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to unreserve.
        """
        return self._action('os-unreserve', volume_id, **kwargs)

    def begin_detaching(self, volume_id, **kwargs):
        """Begin detaching this volume.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to detach.
        """
        return self._action('os-begin_detaching', volume_id, **kwargs)

    def roll_detaching(self, volume_id, **kwargs):
        """Roll detaching this volume.

        :param volume_id: The :class:`Volume` (or its ID)
                          you would like to roll detaching.
        """
        return self._action('os-roll_detaching', volume_id, **kwargs)

    def initialize_connection(self, volume_id, connector, **kwargs):
        """Initialize a volume connection.

        :param volume_id: The :class:`Volume` (or its ID).
        :param connector: connector dict from nova.
        """
        return self._action('os-initialize_connection', volume_id,
                            {'connector': connector}, **kwargs)

    def terminate_connection(self, volume_id, connector, **kwargs):
        """Terminate a volume connection.

        :param volume_id: The :class:`Volume` (or its ID).
        :param connector: connector dict from nova.
        """
        return self._action('os-terminate_connection', volume_id,
                     {'connector': connector}, **kwargs)

    def set_metadata(self, volume_id, metadata, **kwargs):
        """Update/Set a volumes metadata.

        :param volume_id: The :class:`Volume`.
        :param metadata: A list of keys to be set.
        """
        body = {'metadata': metadata}
        return self._post("/volumes/%s/metadata" % volume_id, body = body, 
                          **kwargs)

    def delete_metadata(self, volume_id, key, **kwargs):
        """Delete specified key from volumes metadata.

        :param volume_id: The :class:`Volume`.
        :param keys: A string of key to be removed.
        """
        return self._delete("/volumes/%s/metadata/%s" % (volume_id, key), 
                            **kwargs)

    def update_all_metadata(self, volume_id, metadata, **kwargs):
        """Update all metadata of a volume.

        :param volume_id: The :class:`Volume`.
        :param metadata: A list of keys to be updated.
        """
        body = {'metadata': metadata}
        return self._put("/volumes/%s/metadata" % volume_id, body = body, 
                         **kwargs)

    def upload_to_image(self, volume_id, force, image_name, container_format,
                        disk_format, **kwargs):
        """Upload volume to image service as image.

        :param volume_id: The :class:`Volume` to upload.
        """
        return self._action('os-volume_upload_image',
                            volume_id,
                            {'force': force,
                            'image_name': image_name,
                            'container_format': container_format,
                            'disk_format': disk_format}, **kwargs)

    def force_delete(self, volume_id, **kwargs):
        return self._action('os-force_delete', volume_id, **kwargs)

    def reset_state(self, volume_id, state, **kwargs):
        """Update the provided volume with the provided state.

        :param volume_id: ID of the volume.
        :param state: Volume state.
        """
        return self._action('os-reset_status', volume_id, {'status': state}, 
                            **kwargs)

    def extend(self, volume_id, new_size, **kwargs):
        """Extend the volume size.

        :param volume_id: ID of the volume.
        :param new_size: New volume size.
        """
        return self._action('os-extend',
                            volume_id,
                            {'new_size': new_size}, **kwargs)

    def get_encryption_metadata(self, volume_id, **kwargs):
        """
        Retrieve the encryption metadata from the desired volume.

        :param volume_id: the id of the volume to query
        :return: a dictionary of volume encryption metadata
        """
        return self._get("/volumes/%s/encryption" % volume_id, **kwargs)

    def migrate_volume(self, volume_id, host, force_host_copy, **kwargs):
        """Migrate volume to new host.

        :param volume_id: The :class:`Volume` to migrate
        :param host: The destination host
        :param force_host_copy: Skip driver optimizations
        """
        return self._action('os-migrate_volume',
                            volume_id,
                            {'host': host, 'force_host_copy': force_host_copy}, 
                            **kwargs)

    def migrate_volume_completion(self, old_volume_id, new_volume_id, error, 
                                  **kwargs):
        """Complete the migration from the old volume to the temp new one.

        :param old_volume: The original :class:`Volume` in the migration
        :param new_volume: The new temporary :class:`Volume` in the migration
        :param error: Inform of an error to cause migration cleanup
        """
        return self._action('os-migrate_volume_completion',
                            old_volume_id,
                            {'new_volume': new_volume_id, 'error': error}, 
                            **kwargs)

    def update_readonly_flag(self, volume_id, flag, **kwargs):
        return self._action('os-update_readonly_flag',
                            volume_id,
                            {'readonly': flag}, **kwargs)

    def retype(self, volume_id, volume_type, policy, **kwargs):
        """Change a volume's type.

        :param volume_id: The :class:`Volume` to retype
        :param volume_type: New volume type
        :param policy: Policy for migration during the retype
        """
        return self._action('os-retype',
                            volume_id,
                            {'new_type': volume_type,
                             'migration_policy': policy}, **kwargs)

    def set_bootable(self, volume_id, flag, **kwargs):
        return self._action('os-set_bootable',
                            volume_id,
                            {'bootable': flag}, **kwargs)

    def manage(self, host, ref, name=None, description=None,
               volume_type=None, availability_zone=None, metadata=None,
               bootable=False, **kwargs):
        body = {'volume': {'host': host,
                           'ref': ref,
                           'name': name,
                           'description': description,
                           'volume_type': volume_type,
                           'availability_zone': availability_zone,
                           'metadata': metadata,
                           'bootable': bootable
                           }}
        return self._post('/os-volume-manage', body, 'volume', **kwargs)

    def unmanage(self, volume_id, **kwargs):
        """Unmanage a volume."""
        return self._action('os-unmanage', volume_id, None, **kwargs)
