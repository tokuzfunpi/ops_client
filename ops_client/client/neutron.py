from ops_client.client.base import BaseClient
from ops_client.project.neutron import *

class NeutronClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.agents = AgentManager(self)
        self.quota = QuotaManager(self)
        self.ports = PortManager(self)
        self.extensions = ExtensionManager(self)
        self.networks = NetworkManager(self)
        self.subnets = SubnetManager(self)
        self.routers = RouterManager(self)
        self.floatingips = FloatingIPManager(self)
        self.security_groups = SecurityGroupManager(self)
        self.vpn = VPNManager(self)
        self.ipsec_site = IpsecSiteManager(self)
        self.ike_policy = IKEPolicyManager(self)
        self.ipsec_policy = IpsecPolicyManager(self)
        self.qos_queue = QosQueueManager(self)
        self.network_gateways = NetworkGatewayManager(self)
        self.gateway_devices = GatewayDeviceManager(self)
        self.dhcp = DHCPManager(self)
        self.l3 = L3Manager(self)
        self.firewall_rule = FirewallRuleManager(self)
        self.firewall_policy = FirewallPolicyManager(self)
        self.firewall = FirewallManager(self)
        self.service_provider = ServiceProviderManager(self)
        #self.credentials = CredentialsManager(self)
        self.network_profile = NetworkProfileManager(self)
        self.policy_profile = PolicyProfileManager(self)
        self.metering_labels = MeteringLabelManager(self)
        self.net_partition = NetPartitionManager(self)
        self.packet_filter = PacketFilterManager(self)
