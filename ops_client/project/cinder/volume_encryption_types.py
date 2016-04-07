from ops_client.manager.cinder import CinderBaseManager

class VolumeEncryptionTypeManager(CinderBaseManager):

    def list(self, search_opts=None, **kwargs):
        """
        List all volume encryption types.

        :param volume_types: a list of volume types
        :return: a list of :class: VolumeEncryptionType instances
        """
        # Since the encryption type is a volume type extension, we cannot get
        # all encryption types without going through all volume types.
        resp, _volume_types = self.api.volume_types.list()
        volume_types = _volume_types['volume_types']
        encryption_types = []
        for volume_type in volume_types:
            resp, encryption_type = self._get("/types/%s/encryption"
                                              % volume_type['id'])
            if encryption_type.get('volume_type_id'):
                encryption_types.append(encryption_type)
        return resp, encryption_types

    def get(self, volume_type_id, **kwargs):
        """
        Get the volume encryption type for the specified volume type.

        :param volume_type: the volume type to query
        :return: an instance of :class: VolumeEncryptionType
        """
        return self._get("/types/%s/encryption" % volume_type_id, **kwargs)

    def create(self, volume_type_id, specs, **kwargs):
        """
        Creates encryption type for a volume type. Default: admin only.

        :param volume_type: the volume type on which to add an encryption type
        :param specs: the encryption type specifications to add
        :return: an instance of :class: VolumeEncryptionType
        """
        body = {'encryption': specs}
        return self._post("/types/%s/encryption" % volume_type_id, 
                          body = body, **kwargs)

    def update(self, volume_type, specs, **kwargs):
        """
        Update the encryption type information for the specified volume type.

        :param volume_type: the volume type whose encryption type information
                            must be updated
        :param specs: the encryption type specifications to update
        :return: an instance of :class: VolumeEncryptionType
        """
        raise NotImplementedError()

    def delete(self, volume_type_id, **kwargs):
        """
        Delete the encryption type information for the specified volume type.

        :param volume_type: the volume type whose encryption type information
                            must be deleted
        """
        return self._delete("/types/%s/encryption/provider" % volume_type_id, 
                            **kwargs)
