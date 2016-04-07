from ops_client.client.designate import DesignateClient
import json

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'


user_name2 = 'hothatch_admin'
user_pwd2 = 'hothatch_admin'
project_name2 = "hothatch_admin"
user_domain2 = 'default'
project_domain2 = 'default'

_client = DesignateClient(interface='public')
_client2 = DesignateClient(interface='public')

_client.authenticate(keystone_url,
                     user_name=user_name,
                     user_pwd=user_pwd,
                     user_domain=user_domain,
                     project_name=project_name,
                     project_domain=project_domain)


_client2.authenticate(keystone_url,
                      user_name=user_name2,
                      user_pwd=user_pwd2,
                      user_domain=user_domain2,
                      project_name=project_name2,
                      project_domain=project_domain2)


"""
test zones  (must create a top level domain before creating a zone)
"""
zone_id = 'eef4a543-ef8a-4fef-8b55-cf75e27d6169'
target_project_id = 'd11201c567384a6cb1303a16813af001'
transfer_id = '0d5b06f3-7b36-4e86-8f41-429c6ac50610'
key = "Y81BTNYK"
accept_transfer_id = '2f3ce894-f2de-48d0-9a25-ce26d0abff2b'
# resp, body = _client.zones.list(prefix='v2')
# resp, body = _client.zones.show(zone_id, prefix='v2')
# resp, body = _client.zones.delete(zone_id, prefix='v2')
# resp, body = _client.zones.create("qaqa.example.com.",
#                                   "joe@example.org", prefix='v2')
# resp, body = _client.zones.update(zone_id, masters=["gg.example.org."],
#                                   email="123@gmail.com", ttl=3400,
#                                   description="a",
#                                   prefix='v2')
# resp, body = _client.zones.abandon(zone_id, prefix='v2')
# resp, body = _client.zones.create_transfer(zone_id, target_project_id,
#                                            prefix='v2')
# resp, body = _client2.zones.show_transfer(transfer_id, prefix='v2')
# resp, body = _client2.zones.list_transfer(, prefix='v2')
# resp, body = _client2.zones.accept_transfer(transfer_id, key, prefix='v2')
# resp, body = _client2.zones.show_accept_transfer(accept_transfer_id,
#                                                  prefix='v2')
# resp, body = _client.zones.delete_transfer(transfer_id, prefix='v2')


"""
test recordset
"""
recordset_id = 'a136826b-669d-45b5-af1e-4a74b594839e'
# resp, body = _client.recordset.list(zone_id, prefix='v2')
# resp, body = _client.recordset.show(zone_id, recordset_id, prefix='v2')
# resp, body = _client.recordset.create(zone_id, "qaqa.example.com.",
#                                       "A", records=["10.1.0.2"], prefix='v2')
# resp, body = _client.recordset.update(zone_id, recordset_id,
#                                       ttl=360,
#                                       description="112",
#                                       records=["10.1.0.2", "10.1.0.3"],
#                                       prefix='v2')
# resp, body = _client.recordset.delete(zone_id, recordset_id, prefix='v2')


"""
test tlds
"""
tld_id = "5cc7d560-45de-441e-b1f3-873f652a23e0"
# resp, body = _client.tld.list(prefix='v2')
# resp, body = _client.tld.show(tld_id, prefix='v2')
# resp, body = _client.tld.create(name="org", prefix='v2')
# resp, body = _client.tld.update(tld_id, name="kk", description="aa",
#                                 prefix='v2')
# resp, body = _client.tld.delete(tld_id, prefix='v2')

"""
test blacklists
"""
blacklist_id = "b3b80daf-b603-40af-b231-24d0d1421408"
# resp, body = _client.blacklist.list(, prefix='v2')
# resp, body = _client.blacklist.show(blacklist_id, prefix='v2')
# resp, body = _client.blacklist.create(pattern="test", prefix='v2')
# resp, body = _client.blacklist.update(blacklist_id, pattern="k", prefix='v2')
# resp, body = _client.blacklist.delete(blacklist_id, prefix='v2')

"""
test quotas
"""
# resp, body = _client.quota.show(prefix='v1')


"""
test pool
"""
pool_id = "ff0010f5-7203-41c8-a0ba-ad1ae1149120"
# resp, body = _client.pool.list(prefix='v2')
# resp, body = _client.pool.show(pool_id, prefix='v2')
# resp, body = _client.pool.create(
#     name="test2",
    # ns_records=[
    #     {
    #         "hostname": "ns2.example.org.",
    #         "priority": 10
    #     }
    # ])
# resp, body = _client.pool.update(
#     pool_id,
#     name="1231",
#     ns_records=[
#         {
#             "hostname": "nsdfd.example.org.",
#             "priority": 9
#         }
#     ],
#     attributes={"123": "12"},
#     description="1222")
# resp, body = _client.pool.delete(pool_id, prefix='v2')

"""
test nameservers
"""
# resp, body = _client.nameserver.list(prefix='v2')

"""
test dns limit
"""
# resp, body = _client.dns_limit.list(prefix='v2')

"""
test floating ip
"""
# resp, body = _client.floatingip.list()  # http(500)


"""
test dns tenant
"""
# resp, body = _client.dns_tenant.list(prefix='v1')

"""
test dns count
"""
# resp, body = _client.dns_count.list(prefix='v1')


print resp, json.dumps(body, indent=4)
