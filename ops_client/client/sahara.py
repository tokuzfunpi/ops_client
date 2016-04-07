from ops_client.client.base import BaseClient
from ops_client.project.sahara import *


class SaharaClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.cluster_template = ClusterTemplateManager(self)
        self.clusters = ClusterManager(self)
        self.data_sources = DataSourceManager(self)
        self.images = ImageManager(self)
        self.job_binaries = JobBinaryManager(self)
        self.job_binary_int = JobBinaryInternalManager(self)
        self.job_executions = JobExecutionManager(self)
        self.job_types = JobTypeManager(self)
        self.jobs = JobManager(self)
        self.ng_template = NodeGroupTemplateManager(self)
        self.plugins = PluginManager(self)
