from ops_client.client.base import BaseClient
from ops_client.project.nova import *

class NovaClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.agents = AgentManager(self)
        self.aggregates = AggregateManager(self)
        self.availability_zones = AvailabilityZoneManager(self)
        #self.certs = CertificateManager(self)
        #self.cloudpipe = CloudpipeManager(self)
        #self.fixed_ips = FixedIPsManager(self)
        self.flavor_access = FlavorAccessManager(self)
        self.flavors = FlavorManager(self)
        #self.floating_ip_dns_domain = FloatingIPDNSDomainManager(self)
        #self.floating_ip_dns_entry = FloatingIPDNSEntryManager(self)
        self.floating_ip_pools = FloatingIPPoolManager(self)
        self.floating_ips = FloatingIPManager(self)
        #self.floating_ips_bulk = FloatingIPBulkManager(self)
        #self.fping = FpingManager(self)
        self.hosts = HostManager(self)
        self.hypervisors = HypervisorManager(self)
        self.images = ImageManager(self)
        self.keypairs = KeypairManager(self)
        self.limits = LimitsManager(self)
        self.networks = NetworkManager(self)
        self.quota_classes = QuotaClassSetManager(self)
        self.quotas = QuotaSetManager(self)
        #self.security_group_rules = SecurityGroupRuleManager(self)
        #self.security_groups = SecurityGroupManager(self)
        #self.server_groups = ServerGroupsManager(self)
        self.servers = ServerManager(self)
        self.services = ServiceManager(self)
        self.usage = UsageManager(self)
        #self.virtual_interfaces = VirtualInterfaceManager(self)
        self.volume_snapshots = SnapshotManager(self)
        self.volume_types = VolumeTypeManager(self)
        self.volumes = VolumeManager(self)
