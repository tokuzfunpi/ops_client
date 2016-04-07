from ops_client.client.base import BaseClient
from ops_client.project.heat import *

class HeatClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.build_info = BuildInfoManager(self)
        self.events = EventManager(self)
        self.resource_types = ResourceTypeManager(self)
        self.resources = ResourceManager(self)
        self.services = ServiceManager(self)
        self.snapshots = SnapshotManager(self)
        self.software_configs = SoftwareConfigManager(self)
        self.software_deployments = SoftwareDeploymentManager(self)
        self.stack_actions = StackActionManager(self)
        self.stacks = StackManager(self)
        self.template_versions = TemplateVersionManager(self)
        self.templates = TemplateManager(self)
