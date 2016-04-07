from ops_client.manager.manila import ManilaBaseManager


class ShareTypeManager(ManilaBaseManager):
    """Manage :class:`ShareType` resources."""

    def list(self, **kwargs):
        """Get a list of all share types.

        :rtype: list of :class:`ShareType`.
        """
        return self._get("/types", **kwargs)

    def get(self, share_type_id="default", **kwargs):
        """Get a specific share type.

        :param share_type: The ID of the :class:`ShareType` to get.
        :rtype: :class:`ShareType`
        """
        return self._get("/types/%s" % share_type_id, **kwargs)

    def delete(self, share_type_id, **kwargs):
        """Delete a specific share_type.

        :param share_type: ShareType ID.
        """
        return self._delete("/types/%s" % share_type_id, **kwargs)

    def create(self, name, spec_driver_handles_share_servers,
               spec_snapshot_support=True, is_public=True, **kwargs):
        """Create a share type.

        :param name: Descriptive name of the share type
        :rtype: :class:`ShareType`
        """

        body = {
            "share_type": {
                "name": name,
                "os-share-type-access:is_public": is_public,
                "extra_specs": {
                    "driver_handles_share_servers":
                        spec_driver_handles_share_servers,
                    "snapshot_support": spec_snapshot_support,
                },
            }
        }

        return self._post("/types", body, **kwargs)

    def get_extra_specs(self, share_type_id, **kwargs):
        """Get a specific share type.

        :param share_type: The ID of the :class:`ShareType` to get.
        :rtype: :class:`ShareType`
        """
        return self._get("/types/%s/extra_specs" % share_type_id, **kwargs)

    def set_extra_specs(self, share_type_id, metadata, **kwargs):
        """Get a specific share type.

        :param share_type: The ID of the :class:`ShareType` to get.
        :rtype: :class:`ShareType`
        """
        body = {'extra_specs': metadata}
        return self._post("/types/%s/extra_specs" % share_type_id, body,
                          **kwargs)

    def unset_extra_specs(self, share_type_id, key, **kwargs):
        return self._delete("/types/%s/extra_specs/%s" % (share_type_id, key),
                            **kwargs)

    def list_type_access(self, share_type_id, **kwargs):
        return self._get("/types/%s/os-share-type-access" % share_type_id,
                         **kwargs)

    def add_type_access(self, share_type_id, tenant_id, **kwargs):
        body = {
            'addProjectAccess': {
                'project': tenant_id
            }
        }
        return self._post("/types/%s/action" % share_type_id, body,
                          **kwargs)

    def remove_type_access(self, share_type_id, tenant_id, **kwargs):
        body = {
            'removeProjectAccess': {
                'project': tenant_id
            }
        }
        return self._post("/types/%s/action" % share_type_id, body,
                          **kwargs)
