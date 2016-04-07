from ops_client.manager.cinder import CinderBaseManager


class QoSSpecsManager(CinderBaseManager):

    def list(self, **kwargs):
        """Get a list of all qos specs.

        :rtype: list of :class:`QoSSpecs`.
        """
        return self._get("/qos-specs", **kwargs)

    def get(self, qos_specs_id, **kwargs):
        """Get a specific qos specs.

        :param qos_specs_id: The ID of the :class:`QoSSpecs` to get.
        :rtype: :class:`QoSSpecs`
        """
        return self._get("/qos-specs/%s" % qos_specs_id, **kwargs)

    def delete(self, qos_specs_id, force=False, **kwargs):
        """Delete a specific qos specs.

        :param qos_specs_id: The ID of the :class:`QoSSpecs` to be removed.
        :param force: Flag that indicates whether to delete target qos specs
                      if it was in-use.
        """
        return self._delete("/qos-specs/%s?force=%s" % (qos_specs_id, force), 
                            **kwargs)

    def create(self, name, specs, **kwargs):
        """Create a qos specs.
        :param name: Descriptive name of the qos specs, must be unique
        :param specs: A dict of key/value pairs to be set
        :rtype: :class:`QoSSpecs`
        """

        body = {
            "qos_specs": {
                "name": name,
            }
        }

        body["qos_specs"].update(specs)
        return self._post("/qos-specs", body = body, **kwargs)

    def set_keys(self, qos_specs_id, specs, **kwargs):
        """Update a qos specs with new specifications.

        :param qos_specs_id: The ID of qos specs
        :param specs: A dict of key/value pairs to be set
        :rtype: :class:`QoSSpecs`
        """

        body = {
            "qos_specs": {}
        }

        body["qos_specs"].update(specs)
        return self._put("/qos-specs/%s" % qos_specs_id, body = body, **kwargs)

    def unset_keys(self, qos_specs_id, specs, **kwargs):
        """Update a qos specs with new specifications.

        :param qos_specs_id: The ID of qos specs
        :param specs: A list of key to be unset
        :rtype: :class:`QoSSpecs`
        """
        body = {'keys': specs}

        return self._put("/qos-specs/%s/delete_keys" % qos_specs_id,
                         body = body, **kwargs)

    def get_associations(self, qos_specs_id, **kwargs):
        """Get associated entities of a qos specs.

        :param qos_specs_id: The id of the :class: `QoSSpecs`
        :return: a list of entities that associated with specific qos specs.
        """
        return self._get("/qos-specs/%s/associations" % qos_specs_id, **kwargs)

    def associate(self, qos_specs_id, vol_type_id, **kwargs):
        """Associate a volume type with specific qos specs.

        :param qos_specs_id: The qos specs to be associated with
        :param vol_type_id: The volume type id to be associated with
        """
        return self._get("/qos-specs/%s/associate?vol_type_id=%s" %
                            (qos_specs_id, vol_type_id), **kwargs)

    def disassociate(self, qos_specs_id, vol_type_id, **kwargs):
        """Disassociate qos specs from volume type.

        :param qos_specs_id: The qos specs to be associated with
        :param vol_type_id: The volume type id to be associated with
        """
        return self._get("/qos-specs/%s/disassociate?vol_type_id=%s" %
                            (qos_specs_id, vol_type_id), **kwargs)

    def disassociate_all(self, qos_specs_id, **kwargs):
        """Disassociate all entities from specific qos specs.

        :param qos_specs: The qos specs to be associated with
        """
        return self._get("/qos-specs/%s/disassociate_all" % qos_specs_id, 
                         **kwargs)
