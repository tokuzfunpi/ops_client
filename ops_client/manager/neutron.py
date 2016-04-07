from ops_client.manager.base import BaseManager

class NeutronBaseManager(BaseManager):

    networks_path = "/networks"
    network_path = "/networks/%s"
    ports_path = "/ports"
    port_path = "/ports/%s"
    subnets_path = "/subnets"
    subnet_path = "/subnets/%s"
    quotas_path = "/quotas"
    quota_path = "/quotas/%s"
    extensions_path = "/extensions"
    extension_path = "/extensions/%s"
    routers_path = "/routers"
    router_path = "/routers/%s"
    floatingips_path = "/floatingips"
    floatingip_path = "/floatingips/%s"
    security_groups_path = "/security-groups"
    security_group_path = "/security-groups/%s"
    security_group_rules_path = "/security-group-rules"
    security_group_rule_path = "/security-group-rules/%s"
    vpnservices_path = "/vpn/vpnservices"
    vpnservice_path = "/vpn/vpnservices/%s"
    ipsecpolicies_path = "/vpn/ipsecpolicies"
    ipsecpolicy_path = "/vpn/ipsecpolicies/%s"
    ikepolicies_path = "/vpn/ikepolicies"
    ikepolicy_path = "/vpn/ikepolicies/%s"
    ipsec_site_connections_path = "/vpn/ipsec-site-connections"
    ipsec_site_connection_path = "/vpn/ipsec-site-connections/%s"
    qos_queues_path = "/qos-queues"
    qos_queue_path = "/qos-queues/%s"
    agents_path = "/agents"
    agent_path = "/agents/%s"
    network_gateways_path = "/network-gateways"
    network_gateway_path = "/network-gateways/%s"
    gateway_devices_path = "/gateway-devices"
    gateway_device_path = "/gateway-devices/%s"
    service_providers_path = "/service-providers"
    credentials_path = "/credentials"
    credential_path = "/credentials/%s"
    network_profiles_path = "/network_profiles"
    network_profile_path = "/network_profiles/%s"
    network_profile_bindings_path = "/network_profile_bindings"
    policy_profiles_path = "/policy_profiles"
    policy_profile_path = "/policy_profiles/%s"
    policy_profile_bindings_path = "/policy_profile_bindings"
    metering_labels_path = "/metering/metering-labels"
    metering_label_path = "/metering/metering-labels/%s"
    metering_label_rules_path = "/metering/metering-label-rules"
    metering_label_rule_path = "/metering/metering-label-rules/%s"
    packet_filters_path = "/packet_filters"
    packet_filter_path = "/packet_filters/%s"

    DHCP_NETS = '/dhcp-networks'
    DHCP_AGENTS = '/dhcp-agents'
    L3_ROUTERS = '/l3-routers'
    L3_AGENTS = '/l3-agents'
    firewall_rules_path = "/fw/firewall_rules"
    firewall_rule_path = "/fw/firewall_rules/%s"
    firewall_policies_path = "/fw/firewall_policies"
    firewall_policy_path = "/fw/firewall_policies/%s"
    firewall_policy_insert_path = "/fw/firewall_policies/%s/insert_rule"
    firewall_policy_remove_path = "/fw/firewall_policies/%s/remove_rule"
    firewalls_path = "/fw/firewalls"
    firewall_path = "/fw/firewalls/%s"
    net_partitions_path = "/net-partitions"
    net_partition_path = "/net-partitions/%s"

    # API has no way to report plurals, so we have to hard code them
    EXTED_PLURALS = {'routers': 'router',
                     'floatingips': 'floatingip',
                     'service_types': 'service_type',
                     'service_definitions': 'service_definition',
                     'security_groups': 'security_group',
                     'security_group_rules': 'security_group_rule',
                     'ipsecpolicies': 'ipsecpolicy',
                     'ikepolicies': 'ikepolicy',
                     'ipsec_site_connections': 'ipsec_site_connection',
                     'vpnservices': 'vpnservice',
                     'quotas': 'quota',
                     'service_providers': 'service_provider',
                     'firewall_rules': 'firewall_rule',
                     'firewall_policies': 'firewall_policy',
                     'firewalls': 'firewall',
                     'metering_labels': 'metering_label',
                     'metering_label_rules': 'metering_label_rule',
                     'net_partitions': 'net_partition',
                     'packet_filters': 'packet_filter',
                     }
    # 8192 Is the default max URI len for eventlet.wsgi.server
    MAX_URI_LEN = 8192

    def __init__(self, api):
        self.api = api
        self.url_type = 'neutron_url'
