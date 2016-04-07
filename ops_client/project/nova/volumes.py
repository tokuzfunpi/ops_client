"""
Volume interface.

.. warning::
   Please use cinder-client volume lib instead of use this lib.
"""

from ops_client.manager.nova import NovaBaseManager

class VolumeManager(NovaBaseManager):

    def create(self, size, snapshot_id=None,
                    display_name=None, display_description=None,
                    volume_type=None, availability_zone=None,
                    imageRef=None, response_key = True, **kwargs):
        """
        Create a volume.

        :param size: Size of volume in GB
        :param snapshot_id: ID of the snapshot
        :param display_name: Name of the volume
        :param display_description: Description of the volume
        :param volume_type: Type of volume
        :param availability_zone: Availability Zone for volume
        :rtype: :class:`Volume`
        :param imageRef: reference to an image stored in glance
        """
        body = {'volume': {'size': size,
                            'snapshot_id': snapshot_id,
                            'display_name': display_name,
                            'display_description': display_description,
                            'volume_type': volume_type,
                            'availability_zone': availability_zone,
                            'imageRef': imageRef}}
        if response_key :
            return self._post('/volumes', body, 'volume', **kwargs)
        else :
            return self._post('/volumes', body, **kwargs)

    def get(self, volume_id, response_key = True, **kwargs):
        """
        Get a volume.

        :param volume_id: The ID of the volume to delete.
        :rtype: :class:`Volume`
        """
        if response_key :
            return self._get("/volumes/%s" % volume_id, "volume", **kwargs)
        else :
            return self._get("/volumes/%s" % volume_id, **kwargs)

    def list(self, detailed=True, params=None, response_key = True, **kwargs):
        """
        Get a list of all volumes.

        :rtype: list of :class:`Volume`
        """
        if detailed is True:
            if response_key :
                return self._get("/volumes/detail", "volumes",
                                 params=params, **kwargs)
            else :
                return self._get("/volumes/detail", params=params, **kwargs)
        else:
            if response_key :
                return self._get("/volumes", "volumes", params=params, **kwargs)
            else :
                return self._get("/volumes", params=params, **kwargs)

    def delete(self, volume_id, **kwargs):
        """
        Delete a volume.

        :param volume: The :class:`Volume` to delete.
        """
        return self._delete("/volumes/%s" % volume_id, **kwargs)

    def create_server_volume(self, server_id, volume_id, device,
                             response_key = True, **kwargs):
        """
        Attach a volume identified by the volume ID to the given server ID

        :param server_id: The ID of the server
        :param volume_id: The ID of the volume to attach.
        :param device: The device name
        :rtype: :class:`Volume`
        """
        body = {'volumeAttachment': {'volumeId': volume_id,
                            'device': device}}
        if response_key :
            return self._post("/servers/%s/os-volume_attachments" % server_id,
                body, "volumeAttachment", **kwargs)
        else :
            return self._post("/servers/%s/os-volume_attachments" % server_id,
                body, **kwargs)

    def update_server_volume(self, server_id, attachment_id, new_volume_id,
                             response_key = True, **kwargs):
        """
        Update the volume identified by the attachment ID, that is attached to
        the given server ID

        :param server_id: The ID of the server
        :param attachment_id: The ID of the attachment
        :param new_volume_id: The ID of the new volume to attach
        :rtype: :class:`Volume`
        """
        body = {'volumeAttachment': {'volumeId': new_volume_id}}
        if response_key :
            return self._put("/servers/%s/os-volume_attachments/%s" %
                (server_id, attachment_id,), body, "volumeAttachment", **kwargs)
        else :
            return self._put("/servers/%s/os-volume_attachments/%s" %
                (server_id, attachment_id,), body, **kwargs)

    def get_server_volume(self, server_id, attachment_id,
                          response_key = True, **kwargs):
        """
        Get the volume identified by the attachment ID, that is attached to
        the given server ID

        :param server_id: The ID of the server
        :param attachment_id: The ID of the attachment
        :rtype: :class:`Volume`
        """
        if response_key :
            return self._get("/servers/%s/os-volume_attachments/%s" %
                             (server_id, attachment_id,),
                             "volumeAttachment", **kwargs)
        else :
            return self._get("/servers/%s/os-volume_attachments/%s" %
                             (server_id, attachment_id,), **kwargs)

    def get_server_volumes(self, server_id, response_key = True, **kwargs):
        """
        Get a list of all the attached volumes for the given server ID

        :param server_id: The ID of the server
        :rtype: list of :class:`Volume`
        """
        if response_key :
            return self._get("/servers/%s/os-volume_attachments" % server_id,
                "volumeAttachments", **kwargs)
        else :
            return self._get("/servers/%s/os-volume_attachments" % server_id,
                             **kwargs)

    def delete_server_volume(self, server_id, attachment_id, **kwargs):
        """
        Detach a volume identified by the attachment ID from the given server

        :param server_id: The ID of the server
        :param attachment_id: The ID of the attachment
        """
        return self._delete("/servers/%s/os-volume_attachments/%s" %
                                        (server_id, attachment_id,), **kwargs)
