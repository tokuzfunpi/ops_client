from ops_client.client.base import BaseClient
from ops_client.project.cinder import *

class CinderClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.availability_zones = AvailabilityZoneManager(self)
        self.limits = LimitsManager(self)
        self.qos_spec = QoSSpecsManager(self)
        self.quota_classes = QuotaClassSetManager(self)
        self.quotas = QuotaSetManager(self)
        self.services = ServiceManager(self)
        self.volume_backups = VolumeBackupManager(self)
        self.volume_backups_restore = VolumeBackupRestoreManager(self)
        self.volume_encryption_types = VolumeEncryptionTypeManager(self)
        self.volumes = VolumeManager(self)
        self.volume_snapshots = SnapshotManager(self)
        self.volume_transfers = VolumeTransferManager(self)
        self.volume_types = VolumeTypeManager(self)
