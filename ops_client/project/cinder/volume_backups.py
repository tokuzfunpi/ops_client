from ops_client.manager.cinder import CinderBaseManager

class VolumeBackupManager(CinderBaseManager):

    def create(self, volume_id, container=None,
               name=None, description=None, **kwargs):
        """Creates a volume backup.
        :param volume_id: The ID of the volume to backup.
        :param container: The name of the backup service container.
        :param name: The name of the backup.
        :param description: The description of the backup.
        :rtype: :class:`VolumeBackup`
        """
        body = {'backup': {'volume_id': volume_id,
                           'container': container,
                           'name': name,
                           'description': description}}
        return self._post('/backups', body = body, **kwargs)

    def get(self, backup_id, **kwargs):
        """Show volume backup details.

        :param backup_id: The ID of the backup to display.
        :rtype: :class:`VolumeBackup`
        """
        return self._get("/backups/%s" % backup_id, **kwargs)

    def list(self, detailed=True, **kwargs):
        """Get a list of all volume backups.

        :rtype: list of :class:`VolumeBackup`
        """
        if detailed is True:
            return self._get("/backups/detail", **kwargs)
        else:
            return self._get("/backups", **kwargs)

    def delete(self, backup_id, **kwargs):
        """Delete a volume backup.

        :param backup_id: The :class:`VolumeBackup` to delete.
        """
        return self._delete("/backups/%s" % backup_id, **kwargs)

    def export_record(self, backup_id, **kwargs):
        """Export volume backup metadata record.

        :param backup_id: The ID of the backup to export.
        :rtype: :class:`VolumeBackup`
        """
        return self._get("/backups/%s/export_record" % backup_id, **kwargs)

    def import_record(self, backup_service, backup_url, **kwargs):
        """Export volume backup metadata record.

        :param backup_service: Backup service to use for importing the backup
        :param backup_urlBackup URL for importing the backup metadata
        :rtype: :class:`VolumeBackup`
        """
        body = {'backup-record': {'backup_service': backup_service,
                                  'backup_url': backup_url}}
        return self._post("/backups/import_record", body=body, **kwargs)
