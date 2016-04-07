from ops_client.client.lbaas import LBaaSClient

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_l = LBaaSClient(interface='public')

_l.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)

"""
test_pools:
"""
pool_id = ''
sub_id = ''
# resp, body = _l.pools.list_pools(prefix='lb')
# resp, body = _l.pools.create_pool("ROUND_ROBIN", "TCP", sub_id, prefix='lb')
# resp, body = _l.pools.show_pool(pool_id, prefix='lb')
# resp, body = _l.pools.update_pool(pool_id, pool_body={"name": "test"},
#                                   prefix='lb')
# resp, body = _l.pools.retrieve_pool_stats(pool_id, prefix='lb')
# resp, body = _l.pools.delete_pool(pool_id, prefix='lb')

"""
test_members:
"""
member_id = ''
# resp, body = _l.members.list_members(prefix='lb')
# resp, body = _l.members.create_member(pool_id, "10.90.1.166", "22", prefix='lb')
# resp, body = _l.members.update_member(member_id,
#                                       member_body={"weight": 3},
#                                       prefix='lb')
# resp, body = _l.members.show_member(member_id, prefix='lb')
# resp, body = _l.members.delete_member(member_id, prefix='lb')

"""
test_vips:
"""
vip_id = ''
# resp, body = _l.vips.list_vips(prefix='lb')
# resp, body = _l.vips.create_vip(sub_id, pool_id, 'TCP', 22, prefix='lb')
# resp, body = _l.vips.show_vip(vip_id, prefix='lb')
# resp, body = _l.vips.update_vip(vip_id, member_body={"description": "l"},
#                                 prefix='lb')
# resp, body = _l.vips.delete_vip(vip_id, prefix='lb')

"""
test_lbaas:
"""
lbass_id = ''
# resp, body = _l.lbaas.list_pools_on_lbaas_agent(lbass_id)
# resp, body = _l.lbaas.get_lbaas_agent_hosting_pool(pool_id, prefix='lb')

"""
test_health_monitor:
"""
hm_id = ''
# resp, body = _l.health_monitors.list_health_monitors(prefix='lb')
# resp, body = _l.health_monitors.show_health_monitor(hm_id, prefix='lb')
# resp, body = _l.health_monitors.create_health_monitor("PING", prefix='lb')
# resp, body = _l.health_monitors.update_health_monitor(hm_id,
#                                                       hm_body={"delay": 160},
#                                                       prefix='lb')
# resp, body = _l.health_monitors.associate_health_monitor(hm_id, pool_id,
#                                                          prefix='lb')
# resp, body = _l.health_monitors.disassociate_health_monitor(pool_id, hm_id,
#                                                             prefix='lb')

print 'resp = ', resp
print 'body = ', body
