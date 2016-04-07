from ops_client.client.base import BaseClient
from ops_client.project.manila import *


class ManilaClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.list_ext = ListExtManager(self)
        self.limit = LimitsManager(self)
        self.shares = ShareManager(self)
        self.share_snapshots = ShareSnapshotManager(self)
        self.security_services = SecurityServiceManager(self)
        self.share_servers = ShareServerManager(self)
        self.share_types = ShareTypeManager(self)
        self.scheduler_stats = PoolManager(self)
        self.services = ServiceManager(self)
        self.quotas = QuotaSetManager(self)
        self.availability_zone = AvailabilityZoneManager(self)
