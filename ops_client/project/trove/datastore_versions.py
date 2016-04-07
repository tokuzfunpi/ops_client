from ops_client.manager.trove import TroveBaseManager

class DatastoreVersionManager(TroveBaseManager):

    def list(self, datastore, 
             limit = None, marker = None, response_key = True, **kwargs):
        """Get a list of all datastore versions.

        :rtype: list of :class:`DatastoreVersion`.
        """
        url = self.build_url("/datastores/%s/versions" % datastore,
                            limit = limit,
                            marker = marker)
        if response_key :
            return self._get(url, "versions", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, datastore, datastore_version, response_key = True, **kwargs):
        """Get a specific datastore version.

        :rtype: :class:`DatastoreVersion`
        """
        if response_key :
            return self._get("/datastores/%s/versions/%s" %
                             (datastore, datastore_version),
                             "version", **kwargs)
        else :
            return self._get("/datastores/%s/versions/%s" %
                             (datastore, datastore_version), **kwargs)

    def get_by_uuid(self, datastore_version, response_key = True, **kwargs):
        """Get a specific datastore version.

        :rtype: :class:`DatastoreVersion`
        """
        if response_key :
            return self._get("/datastores/versions/%s" % datastore_version,
                             "version", **kwargs)
        else :
            return self._get("/datastores/versions/%s" % datastore_version,
                             **kwargs)
