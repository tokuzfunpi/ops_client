"""
Volume Type interface.

.. warning::
   Please use cinder-client volume type lib instead of use this lib.
"""

from ops_client.manager.nova import NovaBaseManager

class VolumeTypeManager(NovaBaseManager):

    def list(self, response_key = True, **kwargs):
        """
        Get a list of all volume types.

        :rtype: list of :class:`VolumeType`.
        """
        if response_key :
            return self._get("/types", "volume_types", **kwargs)
        else :
            return self._get("/types", **kwargs)

    def get(self, volume_type_id, response_key = True, **kwargs):
        """
        Get a specific volume type.

        :param volume_type: The ID of the :class:`VolumeType` to get.
        :rtype: :class:`VolumeType`
        """
        if response_key :
            return self._get("/types/%s" % volume_type_id,
                             "volume_type", **kwargs)
        else :
            return self._get("/types/%s" % volume_type_id, **kwargs)

    def delete(self, volume_type_id, **kwargs):
        """
        Delete a specific volume_type.

        :param volume_type: The ID of the :class:`VolumeType` to get.
        """
        return self._delete("/types/%s" % volume_type_id, **kwargs)

    def create(self, name, response_key = True, **kwargs):
        """
        Create a volume type.

        :param name: Descriptive name of the volume type
        :rtype: :class:`VolumeType`
        """
        body = {
            "volume_type": {
                "name": name,
            }
        }

        if response_key :
            return self._post("/types", body, "volume_type", **kwargs)
        else :
            return self._post("/types", body, **kwargs)
