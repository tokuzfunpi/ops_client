from ops_client.client.base import BaseClient
from ops_client.project.lbaas import *

class LBaaSClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.vips = VIPManager(self)
        self.pools = PoolManager(self)
        self.members = MemberManager(self)
        self.health_monitors = HealthMonitorManager(self)
        self.lbaas = LBaaSManager(self)