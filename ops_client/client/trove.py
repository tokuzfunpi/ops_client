from ops_client.client.base import BaseClient
from ops_client.project.trove import *

class TroveClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.backups = BackupManager(self)
        self.clusters = ClusterManager(self)
        self.configurations = ConfigurationManager(self)
        self.configuration_parameters = ConfigurationParameterManager(self)
        self.databases = DatabaseManager(self)
        self.datastores = DatastoreManager(self)
        self.datastore_versions = DatastoreVersionManager(self)
        self.flavors = FlavorManager(self)
        self.instances = InstanceManager(self)
        self.limits = LimitManager(self)
        self.metadata = MetadataManager(self)
        self.root = RootManager(self)
        self.security_groups = SecurityGroupManager(self)
        self.security_group_rules = SecurityGroupRuleManager(self)
        self.users = UserManager(self)