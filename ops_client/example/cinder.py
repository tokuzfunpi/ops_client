from ops_client.client.cinder import CinderClient

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_c = CinderClient(interface='public')

_c.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)

"""
test_volume:
"""
vol_id = ''
instance_id = ''
# resp, body = _c.volumes.create(20)
# resp, body = _c.volumes.get(vol_id)
# resp, body = _c.volumes.list()
# resp, body = _c.volumes.attach(vol_id, instance_id, '/dev/vdb')
# resp, body = _c.volumes.detach(vol_id)
# resp, body = _c.volumes.reserve(vol_id)
# resp, body = _c.volumes.begin_detaching(vol_id)
# resp, body = _c.volumes.roll_detaching(vol_id)
# resp, body = _c.volumes.unreserve(vol_id)
# resp, body = _c.volumes.initialize_connection(vol_id, {})
# resp, body = _c.volumes.terminate_connection(vol_id, {})
# resp, body = _c.volumes.set_metadata(vol_id, {'aaa': 'bbb'})
# resp, body = _c.volumes.delete_metadata(vol_id, 'aaa')
# resp, body = _c.volumes.reset_state(vol_id, 'available')
# resp, body = _c.volumes.extend(vol_id, 30)
# resp, body = _c.volumes.get_encryption_metadata(vol_id)
# resp, body = _c.volumes.update_all_metadata(vol_id,
#     {'aaa':'aaa','bbb':'bbb','ccc':'ccc'})
# resp, body = _c.volumes.update_readonly_flag(vol_id, 'True')
# resp, body = _c.volumes.set_bootable(vol_id, False)
# resp, body = _c.volumes.unmanage(vol_id)  # will delete volume
# resp, body = _c.volumes.delete(vol_id)
# resp, body = _c.volumes.force_delete(vol_id)
# resp, body = _c.volumes.upload_to_image(vol_id,
#                                         'test',
#                                         'test_img',
#                                         'bare',
#                                         'qcow2')
# (can't not get image.)
# resp, body = _c.volumes.update(vol_id, {'description': 'test'})
# resp, body = _c.volumes.migrate_volume()  # not test
# resp, body = _c.volumes.migrate_volume_completion() # not test
# resp, body = _c.volumes.retype(vol_id) # not test
# resp, body = _c.volumes.manage('test2@glusterfs1',
#                                {'source_volume_name':'glusterfs2',
#                                 'source_volume_id':vol_id},
#                                 name='haha')  # not test


"""
test_volume_type:
"""
type_id = ''
# resp, body = _c.volume_types.create('glusterfs1')
# resp, body = _c.volume_types.create('glusterfss', public=True, description="kk")
# resp, body = _c.volume_types.list()
# resp, body = _c.volume_types.get(type_id)
# resp, body = _c.volume_types.delete(type_id)

"""
test_volume_transfers:
"""
trans_id = ''
auth_key = ''
# resp, body = _c.volume_transfers.list(detailed=False)
# resp, body = _c.volume_transfers.create(vol_id)
# resp, body = _c.volume_transfers.get(trans_id)
# resp, body = _c.volume_transfers.accept(trans_id, auth_key)
# (get auth_key from transfer.create)
# resp, body = _c.volume_transfers.delete(trans_id)

"""
test_service:
"""
host = ''
binary = ''
# resp, body = _c.services.list()
# resp, body = _c.services.disable(host, binary)
# get host and binary from list
# resp, body = _c.services.disable_log_reason(host, binary, "node fail")
# resp, body = _c.services.enable(host, binary)

"""
test_quota:
"""
admin_id = ''
# resp, body = _c.quotas.get(admin_id)
# resp, body = _c.quotas.defaults(admin_id)
# resp, body = _c.quotas.update(admin_id, {'volumes':30})
# resp, body = _c.quotas.delete(admin_id)

"""
test_quota_class:
"""
# resp, body = _c.quota_classes.get('aaa')
# resp, body = _c.quota_classes.update('aaa', {'volume': 50})

"""
test_limits:
"""
# resp, body = _c.limits.get()

"""
test_availability_zones:
"""
# resp, body = _c.availability_zones.list()

"""
test_qos_spec:
"""
qos_id = ''
# resp, body = _c.qos_spec.create('test', {"aa": "aa", "bb": "bb"})
# resp, body = _c.qos_spec.list()
# resp, body = _c.qos_spec.get(qos_id)
# resp, body = _c.qos_spec.set_keys(qos_id, {"cc": "cc"})
# resp, body = _c.qos_spec.unset_keys(qos_id, ["aa"])
# resp, body = _c.qos_spec.get_associations(qos_id)
# resp, body = _c.qos_spec.associate(qos_id, type_id)
# resp, body = _c.qos_spec.disassociate(qos_id, type_id)
# resp, body = _c.qos_spec.disassociate_all(qos_id)
# resp, body = _c.qos_spec.delete(qos_id)

"""
test_volume_encryption_types:
"""
# resp, body = _c.volume_encryption_types.list()
# resp, body = _c.volume_encryption_types.get(type_id)
# resp, body = _c.volume_encryption_types.create(
#     type_id, {'provider': 'Test', 'key_size': None, 'cipher': None,
#               'control_location': 'front-end'})
# resp, body = _c.volume_encryption_types.update(
#     type_id, {'provider': 'aaa', 'key_size': None, 'cipher': None,
#               'control_location': 'front-end'})  # not implement
# resp, body = _c.volume_encryption_types.delete(type_id)

"""
test_volume_backups:
"""
# not test
# resp, body = _c.volume_backups.create(vol_id) # (cinder-backup not use.)

"""
test_volume_backups_restore:
"""
# not test

"""
test_volume_snapshot:
"""
snap_id = ''
# resp, body = _c.volume_snapshots.create(vol_id)
# resp, body = _c.volume_snapshots.get(snap_id)
# resp, body = _c.volume_snapshots.list()
# resp, body = _c.volume_snapshots.update(snap_id, updates={"description": "tt"})
# resp, body = _c.volume_snapshots.reset_state(snap_id, "creating")
# ([creating/available/deleting/error/error_deleting])
# resp, body = _c.volume_snapshots.update_snapshot_status(snap_id,
#                                                         {"status": "available"})
# (can use in creating state)
# resp, body = _c.volume_snapshots.set_metadata(snap_id, {"aaa": "bbb"})
# resp, body = _c.volume_snapshots.update_all_metadata(snap_id,
#                                                      {"aaa": "aaa",
#                                                       "bbb": "bbb",
#                                                       "ccc": "ccc"})
# resp, body = _c.volume_snapshots.delete_metadata(snap_id, "bbb")
# key must be a string

print 'resp = ',resp
print 'body = ',body
