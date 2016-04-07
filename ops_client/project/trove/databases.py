from ops_client.manager.trove import TroveBaseManager

class DatabaseManager(TroveBaseManager):

    def create(self, instance, databases, **kwargs):
        """Create new databases within the specified instance."""
        body = {"databases": databases}
        return self._post("/instances/%s/databases" % instance,
                          body, **kwargs)

    def delete(self, instance, dbname, **kwargs):
        """Delete an existing database in the specified instance."""
        return self._delete("/instances/%s/databases/%s" % (instance, dbname),
                            **kwargs)

    def list(self, instance, limit = None, marker = None,
             response_key = True, **kwargs):
        """Get a list of all Databases from the instance.

        :rtype: list of :class:`Database`.
        """
        url = self.build_url("/instances/%s/databases" % instance,
                             limit = limit,
                             marker = marker)
        if response_key :
            return self._get(url, "databases", **kwargs)
        else :
            return self._get(url, **kwargs)