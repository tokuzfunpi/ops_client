from ops_client.client.nova import NovaClient
import time
import datetime

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_n = NovaClient(interface='public')

_n.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)

cirros_id = ''
ubuntu_id = ''
base_id = ''
int_id = ''

"""
test_server:
"""
instance1_id = ''
instance2_id = ''
# resp, body = _n.servers.create('vm1', ubuntu_id,
#                                '3', meta={'testmeta': 'testtttt'},
#                                nics=[{'net-id': int_id}])
# resp, body = _n.servers.create('vm2', cirros_id,
#                                '3', meta={'testmeta': 'testtttt'},
#                                nics=[{'net-id': int_id}])
# resp, body = _n.servers.get(instance1_id)
# resp, body = _n.servers.list()
# resp, body = _n.servers.add_fixed_ip(instance1_id, int_id)
# resp, body = _n.servers.remove_fixed_ip(instance1_id, '192.168.200.24')
# resp, body = _n.servers.add_floating_ip(instance2_id, '10.55.66.42')
# resp, body = _n.servers.add_floating_ip(instance1_id, '10.55.66.42',
#                                         fixed_address='192.168.200.25')
# resp, body = _n.servers.remove_floating_ip(instance1_id, '10.55.66.42')
# body = _n.servers.get_vnc_console(instance1_id, 'spice-html5')  # (not test)
# body = _n.servers.get_spice_console(instance1_id, 'spice-html5')  # (not test)
# body = _n.servers.get_rdp_console(instance1_id, 'rdp-html5')  # (not test)
# body = _n.servers.get_password(instance1_id)
# resp, body = _n.servers.clear_password(instance1_id)
# resp, body = _n.servers.stop(instance2_id)
# resp, body = _n.servers.start(instance2_id)
# resp, body = _n.servers.pause(instance1_id)
# resp, body = _n.servers.unpause(instance1_id)
# resp, body = _n.servers.lock(instance1_id)
# resp, body = _n.servers.unlock(instance1_id)
# resp, body = _n.servers.suspend(instance1_id)  # (qemu bug)
# resp, body = _n.servers.resume(instance1_id)
# resp, body = _n.servers.rescue(instance1_id)
# resp, body = _n.servers.unrescue(instance1_id)
# resp, body = _n.servers.shelve(instance1_id)
# resp, body = _n.servers.shelve_offload(instance1_id) # (not test)
# resp, body = _n.servers.unshelve(instance1_id)
# resp, body = _n.servers.diagnostics(instance1_id)
# resp, body = _n.servers.update(instance1_id, name='update')
# resp, body = _n.servers.change_password(instance1_id, 'test')
# (501) not implement
# resp, body = _n.servers.delete(instance2_id)
# resp, body = _n.servers.reboot(instance1_id)
# resp, body = _n.servers.rebuild(instance1_id, base_id)  # (404)
# resp, body = _n.servers.migrate(instance1_id)  # (not test)
# resp, body = _n.servers.resize(instance2_id, '4')  # (not test all attribute)
# resp, body = _n.servers.confirm_resize(instance2_id)  # (not test)
# resp, body = _n.servers.revert_resize(instance2_id) # (not test)
# body = _n.servers.create_image(instance2_id,
#                                'create_image_name',
#                                metadata={'data1': 'data1', 'data2': 'data2'})
# resp, body = _n.servers.backup(instance2_id, 'backup_name', 'backup_type', 1)
# resp, body = _n.servers.set_meta(instance2_id, {'test': 'test'})
# resp, body = _n.servers.set_meta_item(instance2_id, 'test', 'qq')
# body = _n.servers.get_console_output(instance2_id)  # (not test all attribute)
# body = _n.servers.delete_meta(instance2_id, ['test', 'testmeta'])
# resp, body = _n.servers.live_migrate(instance2_id, 'test2', False, False)
# (not test)
# resp, body = _n.servers.reset_state(instance2_id, state='active')
# resp, body = _n.servers.reset_network(instance2_id)
# resp, body = _n.servers.list_security_group(instance2_id)
# resp, body = _n.servers.add_security_group(instance2_id, 'default')
# resp, body = _n.servers.remove_security_group(instance2_id, 'default')
# resp, body = _n.servers.interface_list(instance2_id)
# resp, body = _n.servers.interface_attach(instance2_id)  # (not test)
# resp, body = _n.servers.interface_detach(instance2_id)  # (not test)
# resp, body = _n.servers.evacuate(instance1_id, 'test3', False)  # (not test)

"""
test_agent:
"""
# resp, body = _n.agents.list()
# resp, body = _n.agents.create('test_os', 'test_architecture', 'test_version',
#                               'test_url', 'test_md5hash', 'test_hypervisor')
# resp, body = _n.agents.update('1', 'update_version',
#                               'update_url', 'update_md5hash')
# resp, body = _n.agents.delete('1')

"""
test_aggregate:
"""
# resp, body = _n.aggregates.list()
# resp, body = _n.aggregates.create('test_aggregate', 'nova')
# resp, body = _n.aggregates.get('1', response_key=True)
# resp, body = _n.aggregates.get_details('1', response_key=False)
# resp, body = _n.aggregates.update('1', {'availability_zone': 'test'})
# resp, body = _n.aggregates.add_host('1', 'ubuntu-kilo')
# resp, body = _n.aggregates.remove_host('1', 'ubuntu-kilo')
# resp, body = _n.aggregates.set_metadata('1', {'test': 'test'})
# resp, body = _n.aggregates.delete('3')

"""
test_availability_zone:
"""
# resp, body = _n.availability_zones.list(detailed=False)

"""
test_cert:
"""
# resp, body = _n.certs.get()  # not test
# resp, body = _n.certs.create()  # not test

"""
test_cloudpipe:
"""
# resp, body = _n.cloudpipe.list()  # not test
# resp, body = _n.cloudpipe.create(project_id)  # not test
# resp, body = _n.cloudpipe.update('10.90.0.149', '8888')  # not test

"""
test_fixed_ips:
"""
# resp, body = _n.fixed_ips.get(fixed_ip_id)  # not test
# resp, body = _n.fixed_ips.reserve(fixed_ip_id)  # not test
# resp, body = _n.fixed_ips.unreserve(fixed_ip_id)  # not test

"""
test_flavor:
"""
# resp, body = _n.flavors.list(detailed=False)
# resp, body = _n.flavors.create('test','4','2','20', is_public=False)
# resp, body = _n.flavors.get('5d44929b-66b0-4614-b563-56a33e6cea12')
# resp, body = _n.flavors.delete('5d44929b-66b0-4614-b563-56a33e6cea12')


"""
test_flavor_access:
"""
flavor_id = ''
admin_id = ''
# resp, body = _n.flavor_access.list(flavor_id)
# resp, body = _n.flavor_access.add_tenant_access(flavor_id, admin_id)
# resp, body = _n.flavor_access.remove_tenant_access(flavor_id, admin_id)

"""
test_floating_ip_dns_domain:
"""
# resp, body = _n.floating_ip_dns_domain.domains()  # not test

"""
test_floating_ip_dns_entry:
"""
# not test

"""
test_floating_ip_pools:
"""
# resp, body = _n.floating_ip_pools.list()

"""
test_floating_ips:
"""
pool = ''
floating_ip_id = ''
# resp, body = _n.floating_ips.list()
# resp, body = _n.floating_ips.create(pool=pool)
# resp, body = _n.floating_ips.get(floating_ip_id)
# resp, body = _n.floating_ips.delete(floating_ip_id)

"""
test_floating_ips_bulk:
"""
# not test

"""
test_fping:
"""
# resp, body = _n.fping.list()  # not test

"""
test_host:
"""
# resp, body = _n.hosts.list()
# resp, body = _n.hosts.get('ubuntu-kilo')
# resp, body = _n.hosts.update('ubuntu-kilo', {'status': 'enable'})  # (501)
# resp, body = _n.hosts.host_action('ubuntu-kilo', 'restart')  # (404)

"""
test_hypervisor:
"""
# resp, body = _n.hypervisors.list(detailed=False)
# resp, body = _n.hypervisors.get('1')
# resp, body = _n.hypervisors.uptime('1')
# resp, body = _n.hypervisors.statistics()
# resp, body = _n.hypervisors.search('ubuntu-kilo')

"""
test_image:
"""
# resp, body = _n.images.list(detailed=False, params={'limit': 1})
# resp, body = _n.images.get(cirros_id)
# resp, body = _n.images.set_meta(cirros_id,
#                                 {'username': 'cirros', 'password': 'cubswin:)'})
# resp, body = _n.images.delete_meta(cirros_id, ['username', 'password'])
# resp, body = _n.images.delete('52f1e655-2a5c-48f5-b5a5-24e574a67db4')

"""
test_keypair:
"""
# resp, body = _n.keypairs.create('test_key')  # not test insert public key
# resp, body = _n.keypairs.list()
# resp, body = _n.keypairs.get('test_key')
# resp, body = _n.keypairs.delete('test_key')

"""
test_limit:
"""
project_id = ''
# resp, body = _n.limits.get(params={'reserved': True, 'tenant_id': project_id})

"""
test_network:
"""
# not test all function
# resp, body = _n.networks.list()
# resp, body = _n.networks.create({'label': 'test', 'cidr': '192.168.100.0/24'})
# (500)
# resp, body = _n.networks.add("2393cad4-ea5e-4dba-8ccb-9654469ac7d3")  # 501

"""
test_quotas:
"""
# resp, body = _n.quotas.get(project_id)
# resp, body = _n.quotas.defaults(project_id)
# resp, body = _n.quotas.update(project_id, {"security_groups": 9})
# resp, body = _n.quotas.delete(project_id)

"""
test_quota_classes:
"""
# unknow usage about this part
# resp, body = _n.quota_classes.get('test')
# resp, body = _n.quota_classes.update('test', quota_body={'cores': 9})

"""
test_security_group:
"""
# resp, body = _n.security_groups.create('test2','test_description2')
# resp, body = _n.security_groups.get(sg_id)
# resp, body = _n.security_groups.list()
# resp, body = _n.security_groups.update(sg_id, 'update','update')
# resp, body = _n.security_groups.delete(sg_id)

"""
test_security_group_rule:
"""
# resp, body = _n.security_group_rules.create(sg_id, ip_protocol='TCP',
#                                             cidr='0.0.0.0/0',
#                                             from_port=1,
#                                             to_port=5000,
#                                             group_id=sg_id)
# resp, body = _n.security_group_rules.delete(sg_rule_id)

"""
test_server_groups:
"""
# resp, body = _n.server_groups.create(name='test', policies=['test'])  # not test
# resp, body = _n.server_groups.list()
# resp, body = _n.server_groups.get(server_g_id)  # not test
# resp, body = _n.server_groups.delete(server_g_id)  # not test

"""
test_services:
"""
# resp, body = _n.services.list(binary='nova-compute')
# resp, body = _n.services.list(host='ubuntu-kilo')
# resp, body = _n.services.list()
# resp, body = _n.services.enable('ubuntu-kilo', 'nova-compute')
# resp, body = _n.services.disable('ubuntu-kilo', 'nova-compute')
# resp, body = _n.services.disable_log_reason('ubuntu-kilo', 'nova-compute',
#                                             'node_fail')
# resp, body = _n.services.delete()  # not tested

"""
test_usages:
"""
# resp, body = _n.usage.list(datetime.datetime.now(),
#                            datetime.datetime.now(), detailed=True)
# resp, body = _n.usage.get(admin_id, datetime.datetime.now(),
#                           datetime.datetime.now())

"""
test_virtual_interfaces:
"""
# resp, body = _n.virtual_interfaces.list(instance3_id)  # return 500

"""
test_volume_snapshot:
"""
# only support endpoint v1
vol_id = ''
# resp, body = _n.volume_snapshots.create(vol_id)  # return 404
# resp, body = _n.volume_snapshots.list()  # return 404
# resp, body = _n.volume_snapshots.get(snapshot_id)  # return 404
# resp, body = _n.volume_snapshots.delete(snapshot_id)  # return 404

"""
test_volume_type:
"""
# only support endpoint v1
# resp, body = _n.volume_types.list()  # return 404
# resp, body = _n.volume_types.create('glusterfs1')  # return 404
# resp, body = _n.volume_types.get(vol_id)  # return 404
# resp, body = _n.volume_types.delete(vol_id)  # return 404

"""
test_volume:
"""
# only support endpoint v1
attach_id = ''
new_vol_id = ''
# resp, body = _n.volumes.list()  # return 404
# resp, body = _n.volumes.create('10')  # return 404
# resp, body = _n.volumes.get(vol_id)  # return 404
# resp, body = _n.volumes.create_server_volume(instance2_id, vol_id, '/dev/vdb')
# resp, body = _n.volumes.update_server_volume(
#     instance2_id, attach_id, new_vol_id)  # attach_id is the old volume id
# resp, body = _n.volumes.get_server_volume(instance2_id, attach_id)
# attach_id is the old volume id
# resp, body = _n.volumes.get_server_volumes(instance2_id)
# resp, body = _n.volumes.delete_server_volume(instance2_id, attach_id)
# attach_id is the old volume id

print 'resp = ',resp
print 'body = ',body
