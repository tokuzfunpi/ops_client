from ops_client.manager.trove import TroveBaseManager

class InstanceManager(TroveBaseManager):

    #TODO(SlickNik): Remove slave_of param after updating tests to replica_of
    def create(self, name, flavor_id, volume = None, databases = None,
               users = None, restorePoint = None, availability_zone = None,
               datastore = None, datastore_version = None, nics = None,
               configuration = None,replica_of = None, slave_of = None,
               replica_count = None, response_key = True, **kwargs):
        """Create (boot) a new instance."""

        body = {"instance": {
            "name": name,
            "flavorRef": flavor_id
        }}
        datastore_obj = {}
        if volume:
            body["instance"]["volume"] = volume
        if databases:
            body["instance"]["databases"] = databases
        if users:
            body["instance"]["users"] = users
        if restorePoint:
            body["instance"]["restorePoint"] = restorePoint
        if availability_zone:
            body["instance"]["availability_zone"] = availability_zone
        if datastore:
            datastore_obj["type"] = datastore
        if datastore_version:
            datastore_obj["version"] = datastore_version
        if datastore_obj:
            body["instance"]["datastore"] = datastore_obj
        if nics:
            body["instance"]["nics"] = nics
        if configuration:
            body["instance"]["configuration"] = configuration
        if replica_of or slave_of:
            body["instance"]["replica_of"] = replica_of or slave_of
        if replica_count:
            body["instance"]["replica_count"] = replica_count

        if response_key :
            return self._post("/instances", body, "instance", **kwargs)
        else :
            return self._post("/instances", body, **kwargs)

    def modify(self, instance, configuration = None, **kwargs):
        body = {
            "instance": {
            }
        }
        if configuration is not None:
            body["instance"]["configuration"] = configuration

        return self._put("/instances/%s" % instance, body, **kwargs)

    def edit(self, instance, configuration = None, name = None,
             detach_replica_source = False, remove_configuration = False,
             **kwargs):
        body = {
            "instance": {
            }
        }
        if configuration and remove_configuration:
            raise Exception("Cannot attach and detach configuration "
                            "simultaneously.")
        if remove_configuration:
            body["instance"]["configuration"] = None
        if configuration is not None:
            body["instance"]["configuration"] = configuration
        if name is not None:
            body["instance"]["name"] = name
        if detach_replica_source:
            # TODO(glucas): Remove slave_of after updating trove
            # (see trove.instance.service.InstanceController#edit)
            body["instance"]["slave_of"] = None
            body["instance"]["replica_of"] = None

        return self._patch("/instances/%s" % instance, body, **kwargs)

    def list(self, limit=None, marker=None, include_clustered=False,
             response_key = True, **kwargs):
        """Get a list of all instances.

        :rtype: list of :class:`Instance`.
        """
        query_strings = {}
        if include_clustered:
            query_strings = {'include_clustered': include_clustered}
        url = self.build_url("/instances",
                             limit = limit,
                             marker = marker,
                             query_strings = query_strings)
        if response_key :
            return self._get(url, "instances", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, instance, response_key = True, **kwargs):
        """Get a specific instances.

        :rtype: :class:`Instance`
        """
        if response_key :
            return self._get("/instances/%s" % instance, "instance", **kwargs)
        else :
            return self._get("/instances/%s" % instance, **kwargs)

    def backups(self, instance, limit = None, marker = None,
                response_key = True, **kwargs):
        """Get the list of backups for a specific instance.

        :rtype: list of :class:`Backups`.
        """
        url = self.build_url("/instances/%s/backups" % instance,
                             limit = limit,
                             marker = marker)
        if response_key :
            return self._get(url, "backups", **kwargs)
        else :
            return self._get(url, **kwargs)

    def delete(self, instance, **kwargs):
        """Delete the specified instance.

        :param instance: A reference to the instance to delete
        """
        return self._delete("/instances/%s" % instance, **kwargs)

    def _action(self, instance, body, **kwargs):
        """Perform a server "action" -- reboot/rebuild/resize/etc."""
        return self._post("/instances/%s/action" % instance, body, **kwargs)

    def resize_volume(self, instance, volume_size, **kwargs):
        """Resize the volume on an existing instances."""
        body = {"resize": {"volume": {"size": volume_size}}}
        return self._action(instance, body, **kwargs)

    def resize_instance(self, instance, flavor_id, **kwargs):
        """Resizes an instance with a new flavor."""
        body = {"resize": {"flavorRef": flavor_id}}
        return self._action(instance, body, **kwargs)

    def restart(self, instance, **kwargs):
        """Restart the database instance.

        :param instance: The :class:`Instance` (or its ID) of the database
        instance to restart.
        """
        body = {'restart': {}}
        return self._action(instance, body, **kwargs)

    def configuration(self, instance, response_key = True, **kwargs):
        """Get a configuration on instances.

        :rtype: :class:`Instance`
        """
        if response_key :
            return self._get("/instances/%s/configuration" % instance,
                             "instance", **kwargs)
        else :
            return self._get("/instances/%s/configuration" % instance, **kwargs)

    def promote_to_replica_source(self, instance, **kwargs):
        """Promote a replica to be the new replica_source of its set

        :param instance: The :class:`Instance` (or its ID) of the database
        instance to promote.
        """
        body = {'promote_to_replica_source': {}}
        return self._action(instance, body, **kwargs)

    def eject_replica_source(self, instance, **kwargs):
        """Eject a replica source from its set

        :param instance: The :class:`Instance` (or its ID) of the database
        instance to eject.
        """
        body = {'eject_replica_source': {}}
        return self._action(instance, body, **kwargs)