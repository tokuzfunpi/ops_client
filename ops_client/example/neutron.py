from ops_client.client.neutron import NeutronClient

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_n = NeutronClient(interface='public')

_n.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)

# raise Exception()

"""
test_agent:
"""
l3_id = ''
# resp, body = _n.agents.list_agents()
# resp, body = _n.agents.show_agent(l3_id)
# resp, body = _n.agents.update_agent(l3_id, {})
# resp, body = _n.agents.delete_agent(l3_id)

"""
test_credential:
"""
# resp, body = _n.credentials.list_credentials()  # (404)

"""
test_dhcp:
"""
int_id = ''
dhcp_id = ''
net_id = ''
# resp, body = _n.dhcp.list_dhcp_agent_hosting_networks(int_id)
# resp, body = _n.dhcp.list_networks_on_dhcp_agent(dhcp_id)
# resp, body = _n.dhcp.add_network_to_dhcp_agent(dhcp_id, net_id) # (409)
# resp, body = _n.dhcp.remove_network_from_dhcp_agent(dhcp_id, net_id) # (409)

"""
test_extension:
"""
# resp, body = _n.extensions.list_extensions()
# resp, body = _n.extensions.show_extension('security-group')


"""
test_firewall_rule:
"""
fw_rule_id = ''
# resp, body = _n.firewall_rule.create_firewall_rule(action="allow")
# resp, body = _n.firewall_rule.list_firewall_rules()
# resp, body = _n.firewall_rule.show_firewall_rule(fw_rule_id)
# resp, body = _n.firewall_rule.update_firewall_rule(fw_rule_id)
# resp, body = _n.firewall_rule.delete_firewall_rule(fw_rule_id)

"""
test_firewall_policy:
"""
fw_policy_id = ''
# resp, body = _n.firewall_policy.list_firewall_policies()
# resp, body = _n.firewall_policy.create_firewall_policy()
# resp, body = _n.firewall_policy.show_firewall_policy(fw_policy_id)
# resp, body = _n.firewall_policy.update_firewall_policy(fw_policy_id)
# resp, body = _n.firewall_policy.firewall_policy_insert_rule(fw_policy_id,
#                                                             fw_rule_id)
# resp, body = _n.firewall_policy.firewall_policy_remove_rule(fw_policy_id,
#                                                             fw_rule_id)

"""
test_firewall:
"""
fw_id = ''
# resp, body = _n.firewall.list_firewalls()
# resp, body = _n.firewall.create_firewall(fw_policy_id)
# resp, body = _n.firewall.update_firewall(fw_id)
# resp, body = _n.firewall.delete_firewall(fw_id)

"""
test_port:
"""
port_id = ''
ext_id = ''
# resp, body = _n.ports.list_ports()
# resp, body = _n.ports.show_port(port_id)
# resp, body = _n.ports.create_port(ext_id)
# resp, body = _n.ports.update_port(port_id, {"name": "test"})
# resp, body = _n.ports.delete_port(port_id)

"""
test_floatingip:
"""
floatip_id = ''
port_id = ''
# resp, body = _n.floatingips.list_floatingips()
# resp, body = _n.floatingips.show_floatingip(floatip_id)
# resp, body = _n.floatingips.create_floatingip(ext_id,
#                                               port_id)  # add to int_port
# resp, body = _n.floatingips.update_floatingip(floatip_id, {})
# resp, body = _n.floatingips.delete_floatingip(floatip_id)

"""
test_policy_profile:
"""
# resp, body = _n.policy_profile.list_policy_profile_bindings()  # (404)

"""
test_network
"""
net_id = ''
# resp, body = _n.networks.list_networks()
# resp, body = _n.networks.show_network(net_id)
# resp, body = _n.networks.create_network({})  # input a dict.
# resp, body = _n.networks.update_network(net_id, {"name": "test"})
# resp, body = _n.networks.delete_network(net_id)

"""
test_subnets:
"""
sub_id = ''
# resp, body = _n.subnets.list_subnets()
# resp, body = _n.subnets.show_subnet(sub_id)
# resp, body = _n.subnets.create_subnet(net_id, 4, "192.167.100.0/24")
# resp, body = _n.subnets.update_subnet(sub_id, {"name": "kk"})
# resp, body = _n.subnets.delete_subnet(sub_id)

"""
test_router:
"""
router_id = ''
# resp, body = _n.routers.list_routers()
# resp, body = _n.routers.show_router(router_id)
# resp, body = _n.routers.create_router({})
# resp, body = _n.routers.update_router(router_id, {"name": "test"})
# resp, body = _n.routers.add_interface_router(router_id, {"subnet_id": sub_id})
# resp, body = _n.routers.remove_interface_router(router_id, {"subnet_id":sub_id})
# resp, body = _n.routers.add_gateway_router(router_id, {"network_id": ext_id})
# resp, body = _n.routers.remove_gateway_router(router_id)
# resp, body = _n.routers.delete_router(router_id)

"""
test_l3:
"""
l3_id = ''
# resp, body = _n.l3.list_routers_on_l3_agent(l3_id)
# resp, body = _n.l3.list_l3_agent_hosting_routers(router_id)
# resp, body = _n.l3.add_router_to_l3_agent(l3_id, router_id) # (404)
# resp, body = _n.l3.remove_router_from_l3_agent(l3_id, router_id) # (404)

"""
test_network_profile:
"""
# resp, body = _n.network_profile.list_network_profiles()  # (404)

"""
test_service_provider:
"""
# resp, body = _n.service_provider.list_service_providers()

"""
test_security_groups:
"""
sg_id = ''
sg_rule_id = ''
# resp, body = _n.security_groups.list_security_groups()
# resp, body = _n.security_groups.create_security_group({})
# resp, body = _n.security_groups.update_security_group(sg_id, {"name": "test"})
# resp, body = _n.security_groups.show_security_group(sg_id)
# resp, body = _n.security_groups.create_security_group_rule(sg_id,
#                                                            direction="ingress")
# resp, body = _n.security_groups.list_security_group_rules()
# resp, body = _n.security_groups.show_security_group_rule(sg_rule_id)
# resp, body = _n.security_groups.delete_security_group_rule(sg_rule_id)
# resp, body = _n.security_groups.delete_security_group(sg_id)

"""
test_pools:
"""
pool_id = ''
sub_id = ''
# resp, body = _n.pools.list_pools()
# resp, body = _n.pools.create_pool("ROUND_ROBIN", "TCP", sub_id)
# resp, body = _n.pools.show_pool(pool_id)
# resp, body = _n.pools.update_pool(pool_id)
# resp, body = _n.pools.retrieve_pool_stats(pool_id)
# resp, body = _n.pools.delete_pool(pool_id)

"""
test_members:
"""
member_id = ''
# resp, body = _n.members.list_members()
# resp, body = _n.members.create_member(pool_id, "10.90.1.166","22")
# resp, body = _n.members.update_member(member_id)
# resp, body = _n.members.show_member(member_id)
# resp, body = _n.members.delete_member(member_id)

"""
test_quotas:
"""
user_id = ''
# resp, body = _n.quota.get_quotas_tenant()
# resp, body = _n.quota.list_quotas()
# resp, body = _n.quota.show_quota(user_id)
# resp, body = _n.quota.update_quota(user_id, {"vip": 9})
# resp, body = _n.quota.delete_quota(user_id)

"""
test_vips:
"""
vip_id = ''
# resp, body = _n.vips.list_vips()
# resp, body = _n.vips.create_vip(sub_id,pool_id,'TCP',22)
# resp, body = _n.vips.show_vip(vip_id)
# resp, body = _n.vips.update_vip(vip_id)
# resp, body = _n.vips.delete_vip(vip_id)

"""
test_qos_queue:
"""
# resp, body = _n.qos_queue.list_qos_queues()  # (404)

"""
test_packet_filter:
"""
# resp, body = _n.packet_filter.list_packet_filters()  # (404)

"""
test_network_gateway:
"""
# resp, body = _n.network_gateways.list_network_gateways()  # (404)

"""
test_net_partition:
"""
# resp, body = _n.net_partition.list_net_partitions()  # (404)

"""
test_metering_label:
"""
metering_id = ''
metering_rule_id = ''
# resp, body = _n.metering_labels.list_metering_labels()
# resp, body = _n.metering_labels.create_metering_label()
# resp, body = _n.metering_labels.show_metering_label(metering_id)
# resp, body = _n.metering_labels.delete_metering_label(metering_id)
# resp, body = _n.metering_labels.list_metering_label_rules()
# resp, body = _n.metering_labels.create_metering_label_rule(metering_id,
#                                                            "ingress",
#                                                            "10.90.1.0/23")
# resp, body = _n.metering_labels.show_metering_label_rule(metering_rule_id)
# resp, body = _n.metering_labels.delete_metering_label_rule(metering_rule_id)

"""
test_lbaas:
"""
lbass_id = ''
# resp, body = _n.lbaas.list_pools_on_lbaas_agent(lbass_id)
# resp, body = _n.lbaas.get_lbaas_agent_hosting_pool(pool_id)

"""
test_ipsec_policy:
"""
ipsecpolicy_id = ''
# resp, body = _n.ipsec_policy.list_ipsecpolicies()
# resp, body = _n.ipsec_policy.create_ipsecpolicy()
# resp, body = _n.ipsec_policy.update_ipsecpolicy(ipsecpolicy_id)
# resp, body = _n.ipsec_policy.show_ipsecpolicy(ipsecpolicy_id)
# resp, body = _n.ipsec_policy.delete_ipsecpolicy(ipsecpolicy_id)

"""
test_ikepolicy:
"""
ikepolicy_id = ''
# resp, body = _n.ike_policy.list_ikepolicies()
# resp, body = _n.ike_policy.create_ikepolicy()
# resp, body = _n.ike_policy.update_ikepolicy(ikepolicy_id)
# resp, body = _n.ike_policy.show_ikepolicy(ikepolicy_id)
# resp, body = _n.ike_policy.delete_ikepolicy(ikepolicy_id)

"""
test_vpn:
"""
vpnservice_id = ''
router_id = ''
sub_id = ''
# resp, body = _n.vpn.list_vpnservices()
# resp, body = _n.vpn.create_vpnservice(router_id, sub_id, name='test')
# (status = pending create, after create ipsec_site_connection, status = active)
# resp, body = _n.vpn.update_vpnservice(vpnservice_id, description = "test")  
# (can not use while status = pending create)
# resp, body = _n.vpn.show_vpnservice(vpnservice_id)
# resp, body = _n.vpn.delete_vpnservice(vpnservice_id)

"""
test_ipsec_site_connection:
"""
ipsec_connection_id = ''
# resp, body = _n.ipsec_site.list_ipsec_site_connections()
# resp, body = _n.ipsec_site.create_ipsec_site_connection(ipsecpolicy_id,
#                                                         ikepolicy_id,
#                                                         vpnservice_id,
#                                                         "test",
#                                                         "10.90.1.0/23",
#                                                         "10.90.1.166",
#                                                         "test")
# (show pendint create)
# resp, body = _n.ipsec_site.show_ipsec_site_connection(ipsec_connection_id)
# resp, body = _n.ipsec_site.update_ipsec_site_connection(ipsec_connection_id) 
# (can not update while pending create)
# resp, body = _n.ipsec_site.delete_ipsec_site_connection(ipsec_connection_id)

"""
test_gateway_device:
"""
# resp, body = _n.gateway_devices.list_gateway_devices()  # (404)

"""
test_health_monitor:
"""
hm_id = ''
# resp, body = _n.health_monitors.list_health_monitors()
# resp, body = _n.health_monitors.create_health_monitor("PING")
# resp, body = _n.health_monitors.update_health_monitor(hm_id)
# resp, body = _n.health_monitors.associate_health_monitor(hm_id, pool_id)
# resp, body = _n.health_monitors.disassociate_health_monitor(pool_id, hm_id)

print 'resp = ', resp
print 'body = ', body
