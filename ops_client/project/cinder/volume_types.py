from ops_client.manager.cinder import CinderBaseManager

class VolumeTypeManager(CinderBaseManager):

    def list(self, search_opts=None, **kwargs):
        """Lists all volume types.

        :rtype: list of :class:`VolumeType`.
        """
        return self._get("/types", **kwargs)

    def get(self, volume_type_id, **kwargs):
        """Get a specific volume type.

        :param volume_type_id: The ID of the :class:`VolumeType` to get.
        :rtype: :class:`VolumeType`
        """
        return self._get("/types/%s" % volume_type_id, **kwargs)

    def delete(self, volume_type_id, **kwargs):
        """Deletes a specific volume_type.

        :param volume_type_id: The name or ID of the :class:`VolumeType` to get.
        """
        return self._delete("/types/%s" % volume_type_id, **kwargs)

    def create(self, name, 
               extra_specs = {}, public = True, description = None, **kwargs):
        """Creates a volume type.

        :param name: Descriptive name of the volume type
        :rtype: :class:`VolumeType`
        """

        body = {
            "volume_type": {
                "name": name,
                "extra_specs": extra_specs,
                "os-volume-type-access:is_public": public,
                "description": description
            }
        }

        return self._post("/types", body = body, **kwargs)
