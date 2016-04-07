from ops_client.client.trove import TroveClient

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_id = 'e2211087bf0f44f5a2c4bfd0b78ca317'
project_domain = 'default'

_t = TroveClient()

_t.authenticate(keystone_url,
                user_name=user_name,
                user_pwd=user_pwd,
                user_domain=user_domain,
                project_name=project_name,
                # project_id=project_id,
                project_domain=project_domain)

'''
datastores
'''
datastore_id = '163aa579-ddf0-4067-9d53-bec208cb38a1'
# resp, body = _t.datastores.list()
# resp, body = _t.datastores.get(datastore_id)

'''
datastore_versions
'''
version_id = '95eb192d-8ca6-4b7d-bc1e-3614689b5fd6'
# resp, body = _t.datastore_versions.list(datastore_id)
# resp, body = _t.datastore_versions.get(datastore_id, version_id)
# resp, body = _t.datastore_versions.get_by_uuid(version_id)

'''
backups (not test)
'''

'''
clusters (not test)
'''

'''
configurations
'''
# resp, body = _t.configurations.list()
# resp, body = _t.configurations.create(
#     'test', {"connect_timeout": 120}, datastore=datastore_id,
#     datastore_version=version_id)  # not supported 422
# resp, body = _t.configurations.create(
#     'test', {"test": "kk"}, datastore=datastore_id,
#     datastore_version=version_id)  # not supported 422
'''
configuration_parameters
'''
# resp, body = _t.configuration_parameters.parameters(datastore_id, version_id)
# resp, body = _t.configuration_parameters.get_parameter(
#     datastore_id, version_id, 'ttt')  # not test
# resp, body = _t.configuration_parameters.parameters_by_version(version_id)
# resp, body = _t.configuration_parameters.get_parameter_by_version(
#     version_id, "ttt") # not test
'''
instances
'''
instance_id = '2e4fe3d8-af09-47c7-ad6c-875d2f5adc58'
# network_id = 'acc6cad5-ef3b-49bf-90ea-43dae009a9a3'  # 107
network_id = 'b0c5639d-c7b1-41b4-94a8-6e6a11abd53a'  # 103
# resp, body = _t.instances.list()
# resp, body = _t.instances.get(instance_id)
# resp, body = _t.instances.delete(instance_id)
# resp, body = _t.instances.create(
#     'test', 3, datastore='mysql', datastore_version='5.5',
#     volume={"size": 5}, nics=[{"net-id": network_id}])
# resp, body = _t.instances.modify(instance_id)
# resp, body = _t.instances.edit(instance_id)
# resp, body = _t.instances.backups(instance_id, response_key=False)
# resp, body = _t.instances.resize_volume(instance_id, 10)
# resp, body = _t.instances.resize_instance(instance_id, 2)
# resp, body = _t.instances.restart(instance_id)
# resp, body = _t.instances.configuration(instance_id)
# resp, body = _t.instances.promote_to_replica_source(instance_id)  # not test
# resp, body = _t.instances.eject_replica_source(instance_id )  # not test
'''
databases
'''
# resp, body = _t.databases.list(instance_id)
# resp, body = _t.databases.create(
#     instance_id, [{"name": "db1"}, {"name": "db2"}])
# resp, body = _t.databases.delete(instance_id, 'db5')
'''
flavors
'''
flavor_id = 2
# resp, body = _t.flavors.list()
# resp, body = _t.flavors.get(flavor_id)
# resp, body = _t.flavors.list_datastore_version_associated_flavors(
#     datastore_id, version_id)  # return 404
'''
limits
'''
# resp, body = _t.limits.list()

'''
metadata (not support)
'''
# resp, body = _t.metadata.list(instance_id)
'''
root
'''
# resp, body = _t.root.is_root_enabled(instance_id)
# resp, body = _t.root.create(instance_id)

'''
security_groups
'''
sg_id = '485ea6a7-0fe2-44c4-957e-a880171f2771'
# sg_id = 24
# resp, body = _t.security_groups.list()
# resp, body = _t.security_groups.get(sg_id)

'''
security_group_rules
'''
# group_id = 24
group_id = '485ea6a7-0fe2-44c4-957e-a880171f2771'
# sgr_id = 37
gr_id = 'c46d6278-00f7-401c-bf69-7c24d5963159'
# resp, body = _t.security_group_rules.list(group_id)
# resp, body = _t.security_group_rules.create(group_id, '10.90.0.0/24')
# resp, body = _t.security_group_rules.delete(gr_id)
'''
users
'''
# resp, body = _t.users.list(instance_id)
# resp, body = _t.users.get(instance_id, 'ggg')
# resp, body = _t.users.create(instance_id, [{"name": "kkk", "password": "kk"}])
# resp, body = _t.users.update_attributes(
#     instance_id, 'ggg', newuserattr={"name": "ttt"})
# resp, body = _t.users.list_access(instance_id, 'ttt')
# resp, body = _t.users.grant(instance_id, 'ttt', ['db1', 'db2'])
# resp, body = _t.users.revoke(instance_id, 'ttt', 'db2')
# resp, body = _t.users.change_passwords(
#     instance_id, [{"name": "ttt", "password": "ttt"}])

print 'resp = ',resp
print 'body = ',body