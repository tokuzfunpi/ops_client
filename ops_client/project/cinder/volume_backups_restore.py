from ops_client.manager.cinder import CinderBaseManager

class VolumeBackupRestoreManager(CinderBaseManager):

    def restore(self, backup_id, volume_id=None, **kwargs):
        """Restore a backup to a volume.

        :param backup_id: The ID of the backup to restore.
        :param volume_id: The ID of the volume to restore the backup to.
        :rtype: :class:`Restore`
        """
        body = {'restore': {'volume_id': volume_id}}
        return self._post("/backups/%s/restore" % backup_id, 
                          body = body, **kwargs)
