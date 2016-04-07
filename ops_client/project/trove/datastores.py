from ops_client.manager.trove import TroveBaseManager

class DatastoreManager(TroveBaseManager):

    def list(self, limit = None, marker = None, response_key = True, **kwargs):
        """Get a list of all datastores.

        :rtype: list of :class:`Datastore`.
        """
        url = self.build_url("/datastores", limit = limit, marker = marker)
        if response_key :
            return self._get(url, "datastores", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, datastore, response_key = True, **kwargs):
        """Get a specific datastore.

        :rtype: :class:`Datastore`
        """
        if response_key :
            return self._get("/datastores/%s" % datastore,
                             "datastore", **kwargs)
        else :
            return self._get("/datastores/%s" % datastore, **kwargs)