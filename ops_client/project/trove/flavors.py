from ops_client.manager.trove import TroveBaseManager

class FlavorManager(TroveBaseManager):

    def list(self, response_key = True, **kwargs):
        """Get a list of all flavors.
        :rtype: list of :class:`Flavor`.
        """
        if response_key :
            return self._get("/flavors", "flavors", **kwargs)
        else :
            return self._get("/flavors", **kwargs)

    def list_datastore_version_associated_flavors(
            self, datastore, version_id, response_key = True, **kwargs):
        """Get a list of all flavors for the specified datastore type
        and datastore version .
        :rtype: list of :class:`Flavor`.
        """
        if response_key :
            return self._get("/datastores/%s/versions/%s/flavors" %
                             (datastore, version_id), "flavors", **kwargs)
        else :
            return self._get("/datastores/%s/versions/%s/flavors" %
                             (datastore, version_id), **kwargs)

    def get(self, flavor, response_key = True, **kwargs):
        """Get a specific flavor.

        :rtype: :class:`Flavor`
        """
        if response_key :
            return self._get("/flavors/%s" % flavor, "flavor", **kwargs)
        else :
            return self._get("/flavors/%s" % flavor, **kwargs)