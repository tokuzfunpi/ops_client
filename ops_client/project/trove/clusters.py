from ops_client.manager.trove import TroveBaseManager

class ClusterManager(TroveBaseManager):

    def create(self, name, datastore, datastore_version,
               instances = None, response_key = True, **kwargs):
        """Create (boot) a new cluster."""
        body = {"cluster": {
            "name": name
        }}
        datastore_obj = {
            "type": datastore,
            "version": datastore_version
        }
        body["cluster"]["datastore"] = datastore_obj
        if instances:
            body["cluster"]["instances"] = instances

        if response_key :
            return self._post("/clusters", body, "cluster", **kwargs)
        else :
            return self._post("/clusters", body, **kwargs)

    def list(self, limit = None, marker = None, response_key = True, **kwargs):
        """Get a list of all clusters.

        :rtype: list of :class:`Cluster`.
        """
        url = self.build_url("/clusters", limit = limit, marker = marker)
        if response_key :
            return self._get(url, "clusters", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, cluster, response_key = True, **kwargs):
        """Get a specific cluster.

        :rtype: :class:`Cluster`
        """
        if response_key :
            return self._get("/clusters/%s" % cluster, "cluster", **kwargs)
        else :
            return self._get("/clusters/%s" % cluster, **kwargs)

    def delete(self, cluster, **kwargs):
        """Delete the specified cluster.

        :param cluster: The cluster to delete
        """
        return self._delete("/clusters/%s" % cluster, **kwargs)

    def add_shard(self, cluster, response_key = True, **kwargs):
        """Adds a shard to the specified cluster.

        :param cluster: The cluster to add a shard to
        """
        body = {"add_shard": {}}
        if response_key :
            return self._post("/clusters/%s" % cluster,
                              body, "cluster", **kwargs)
        else :
            return self._post("/clusters/%s" % cluster, body, **kwargs)