from ops_client.manager.trove import TroveBaseManager

class BackupManager(TroveBaseManager):

    def get(self, backup, response_key = True, **kwargs):
        """Get a specific backup.

        :rtype: :class:`Backups`
        """
        if response_key :
            return self._get("/backups/%s" % backup, "backup", **kwargs)
        else : 
            return self._get("/backups/%s" % backup, **kwargs)

    def list(self, limit = None, marker = None, datastore = None,
             response_key = True, **kwargs):
        """Get a list of all backups.

        :rtype: list of :class:`Backups`.
        """
        query_strings = {}
        if datastore:
            query_strings = {'datastore': datastore}
        url = self.build_url("/backups",
                             limit = limit,
                             marker = marker,
                             query_strings = query_strings)
        if response_key :
            return self._get(url, "backups", **kwargs)
        else :
            return self._get(url, **kwargs)

    def create(self, name, instance = None, description = None,
               parent_id = None, backup=None, response_key = True, **kwargs):
        """Create a new backup from the given instance."""
        body = {
            "backup": {
                "name": name
            }
        }

        if instance:
            body['backup']['instance'] = instance
        if backup:
            body["backup"]['backup'] = backup
        if description:
            body['backup']['description'] = description
        if parent_id:
            body['backup']['parent_id'] = parent_id
        if response_key :
            return self._post("/backups", body, "backup", **kwargs)
        else :
            return self._post("/backups", body, **kwargs)

    def delete(self, backup_id, **kwargs):
        """Delete the specified backup.

        :param backup_id: The backup id to delete
        """
        return self._delete("/backups/%s" % backup_id, **kwargs)
