from ops_client.client.manila import ManilaClient
from time import time
import json

keystone_url = 'http://10.55.66.134:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_m = ManilaClient(interface='public')

_m.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)


tenant_id = '6bec2a4965404db990de7942f5b4b645'
user_id = 'be187e41bb2145ab80bdc49e9a501e74'

print _m.token

"""
list extensions:
"""
#list extensions
# resp, body = _m.list_ext.show_all()
"""
Limits:
"""
# resp, body = _m.limit.get()
"""
Share:
"""
share_id = '054226c1-2759-4a93-ba00-23b38e27cfa0'
share2_id = '346c6458-cbc2-4108-8bcf-ea708c609239'
# resp, body = _m.shares.get(share_id)
# resp, body = _m.shares.get(share2_id)
# resp, body = _m.shares.list()

# search_opts = {'status':'error', 'limit': 1}
# resp, body = _m.shares.list()
# search_opts = {'is_public': False, 'status':'error', 'limit': 1}
# resp, body = _m.shares.list(detailed=True, search_opts=search_opts)
# sort_key = 'created_at'
# sort_dir = 'desc'
# resp, body = _m.shares.list(detailed=True,
#                             sort_key=sort_key,
#                             sort_dir=sort_dir)
# _random_t = str(int(time()*1000))[-3:]
# share_proto = 'NFS'
# size = 2
# name = 'test%s' %(_random_t)
# share_type_name = 'hothatch'
# resp, body = _m.shares.create(share_proto,
#                               size,
#                               name=name,
#                               share_type_name=share_type_name)
# update_body = {'display_name':'update_ok'}
# update_body = {'display_description':'kerker'}
# update_body = {'is_public':True}
# resp, body = _m.shares.update('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac',
#                               updates=update_body)
# resp, body = _m.shares.delete(share_id)
"""
Share action
"""
# resp, body = _m.shares.reset_state(share_id,
#                                    'available')
# resp, body = _m.shares.force_delete('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac')
# resp, body = _m.shares.extend(share_id, 6)
# resp, body = _m.shares.shrink(share_id, 4)
'''
{
    "os-allow_access": {
        "access_level": "rw",
        "access_type": "ip",
        "access_to": "0.0.0.0/0"
    }
}
'''
# access_type = 'ip'
# access_to = '0.0.0.0/0'
# access_level = 'rw'
# resp, body = _m.shares.allow(share_id, access_type, access_to, access_level)
'''
resp =  {
    'status': 200,
    'headers': {
        'content-length': '195',
        'x-compute-request-id': 'req-4bc204be-d191-4279-bcc2-8bce138b9e32',
        'vary': 'X-OpenStack-Manila-API-Version',
        'x-openstack-manila-api-version': '2.0',
        'date': 'Fri, 04 Mar 2016 02:57:11 GMT',
        'content-type': 'application/json'
    }
}
body =  {
    'access': {
        'share_id': 'bcaeadd9-03ee-437b-8b82-de2bf810b8f4',
        'access_type': 'ip',
        'access_to': '0.0.0.0/0',
        'access_level': 'rw',
        'state': 'new',
        'id': '00c75b60-91e5-4e10-b075-45b56f7edca4'
    }
}
'''
# access_id = '21f044c8-3792-4ed7-a598-26c4c4f86825'
# resp, body = _m.shares.deny(share_id, access_id) #return 202
# resp, body = _m.shares.access_list(share_id)
"""
Share metadata:
"""
# resp, body = _m.shares.get_metadata('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac')
# metadata = {"key1": "value1"}
# resp, body = _m.shares.set_metadata('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac',
#                                     metadata)
# new_metadata = {"key1": "22222", " key10": "ohoh"} #value cannot be int
# resp, body = _m.shares.update_all_metadata(
#                  '02cb5e3e-6a57-49ed-aec3-c8384c3f0dac', new_metadata)
# resp, body = _m.shares.delete_metadata('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac',
#                                        'key1')
"""
Share snapshot:
"""
# resp, body = _m.share_snapshots.list(detailed=False)
# resp, body = _m.share_snapshots.create('02cb5e3e-6a57-49ed-aec3-c8384c3f0dac',
#                                        name='test_sn')
"""
Security services
"""
# resp, body = _m.security_services.list(detailed=False)
"""
Share servers
"""
# resp, body = _m.share_servers.list()
"""
Share types:
"""
share_type_id = '3e4dee5c-e2a4-43b4-b92d-0c296ef15274'
# resp, body = _m.share_types.list()
'''
{
    "share_types": [
        {
            "extra_specs": {
                "driver_handles_share_servers": "False",
                "snapshot_support": "False"
            },
            "id": "3e4dee5c-e2a4-43b4-b92d-0c296ef15274",
            "name": "hothatch",
            "os-share-type-access:is_public": true,
            "required_extra_specs": {
                "driver_handles_share_servers": "False"
            }
        }
    ],
    "volume_types": [
        {
            "extra_specs": {
                "driver_handles_share_servers": "False",
                "snapshot_support": "False"
            },
            "id": "3e4dee5c-e2a4-43b4-b92d-0c296ef15274",
            "name": "hothatch",
            "os-share-type-access:is_public": true,
            "required_extra_specs": {
                "driver_handles_share_servers": "False"
            }
        }
    ]
}
'''
# resp, body = _m.share_types.get() #default case
# resp, body = _m.share_types.get('79eda475-81b3-47a7-ab12-2fd0e83d5f9f')
# resp, body = _m.share_types.get(share_type_id)
'''
body
{
    "share_type": {
        "extra_specs": {
            "driver_handles_share_servers": "False",
            "snapshot_support": "False"
        },
        "id": "f3b08149-c571-4bf7-b068-e05fc1500538",
        "name": "hothatch",
        "os-share-type-access:is_public": false,
        "required_extra_specs": {}
    },
    "volume_type": {
        "extra_specs": {
            "driver_handles_share_servers": "False",
            "snapshot_support": "False"
        },
        "id": "f3b08149-c571-4bf7-b068-e05fc1500538",
        "name": "hothatch",
        "os-share-type-access:is_public": false,
        "required_extra_specs": {}
    }
}

'''
# resp, body = _m.share_types.delete(share_type_id)
'''
body = {
    "volume_type":{
        "name":"hothatch",
        "extra_specs":{
            "driver_handles_share_servers":False,
            "snapshot_support":False
        }
    }
}
'''
# type_name = 'hothatch'
# spec_driver_handles_share_servers = False
# spec_snapshot_support = False
# is_public = True

# resp, body = _m.share_types.create(type_name, 
#                                    spec_driver_handles_share_servers,
#                                    spec_snapshot_support=spec_snapshot_support,
#                                    is_public=is_public)
#create resp
'''
resp =  {
    'status': 200, 
    'headers': {
        'content-length': '549',
        'x-compute-request-id': 'req-08010d72-10bf-474e-af24-1de4b76c3dbb',
        'vary': 'X-OpenStack-Manila-API-Version',
        'x-openstack-manila-api-version': '2.0',
        'date': 'Fri, 04 Mar 2016 06:11:41 GMT',
        'content-type': 'application/json'
    }
}
body =  {
    'volume_type': {
        'os-share-type-access:is_public': True,
        'required_extra_specs': {
            'driver_handles_share_servers': False
        },
        'extra_specs': {
            'snapshot_support': 'False',
            'driver_handles_share_servers': 'False'
        },
        'name': 'hothatch',
        'id': '5bc7c294-d7a3-4f01-9c68-29042c4d8ea1'
    },
    'share_type': {
        'os-share-type-access:is_public': True, 
        'required_extra_specs': {
            'driver_handles_share_servers': False
        },
        'extra_specs': {
            'snapshot_support': 'False',
            'driver_handles_share_servers': 'False'
        },
        'name': 'hothatch',
        'id': u'5bc7c294-d7a3-4f01-9c68-29042c4d8ea1'
    }
}
'''
# resp, body = _m.share_types.get_extra_specs(share_type_id)
# metadata = {'vendor_name': 'MY'}
# metadata = {'key1': 'value1'}
# resp, body = _m.share_types.set_extra_specs(share_type_id, metadata)
# resp, body = _m.share_types.unset_extra_specs(share_type_id, 'key1') #202
# resp, body = _m.share_types.list_type_access(share_type_id)
# resp, body = _m.share_types.add_type_access(share_type_id, tenant_id) #202
# resp, body = _m.share_types.remove_type_access(share_type_id, tenant_id) #202
"""
Back-end storage pools:
"""
# resp, body = _m.scheduler_stats.list()
# resp, body = _m.scheduler_stats.list(detailed=False)

"""
Services:
"""
# resp, body = _m.services.list()
'''
down hh1ad6db9e
down manila-share
'''
# update_body = {
#     'binary': 'manila-share',
#     'host': 'hh1ad6db9e'
# }
# # update_body = json.dumps(update)
# resp, body = _m.services.enable_service(update_body)
# resp, body = _m.services.disable_service(update_body)

"""
Quotas:
"""
# resp, body = _m.quotas.get(tenant_id)
# get result
# {
#     'quota_set': {
#         'gigabytes': 1000,
#         'shares': 50,
#         'snapshot_gigabytes': 1000,
#         'snapshots': 50,
#         'id': '6bec2a4965404db990de7942f5b4b645',
#         'share_networks': 10
#     }
# }
# resp, body = _m.quotas.get(tenant_id, user_id)
# resp, body = _m.quotas.defaults(tenant_id)
'''
update_quota = {
    "quota_set": {
        "tenant_id": "16e1ab15c35a457e9c2b2aa189f544e1",
        "snapshot_gigabytes": 999,
        "snapshots": 49,
        "share_networks": 9
    }
}
'''
# resp, body = _m.quotas.update(tenant_id, snapshots=49, 
#                               snapshot_gigabytes=999, share_networks=9)
'''
resp =  {
    'status': 200, 
    'headers': {
        'content-length': '113', 
        'x-compute-request-id': 'req-28ca5d0d-0d33-401b-9d68-7712ab0b2143', 
        'vary': 'X-OpenStack-Manila-API-Version', 
        'x-openstack-manila-api-version': '2.0', 
        'date': 'Fri, 04 Mar 2016 05:51:24 GMT', 
        'content-type': 'application/json'
    }
}
body =  {
    'quota_set': {
        'gigabytes': 1000,
        'snapshot_gigabytes': 999,
        'shares': 50,
        'snapshots': 49,
        'share_networks': 9
    }
}
'''

# resp, body = _m.quotas.delete(tenant_id) #return 202


"""
Availability Zone
"""
resp, body = _m.availability_zone.get()


print 'resp = ', resp
print 'body = ', body

# print len(body['services'])
# print 'body len', body['share']['id']
# print 'body len', body['share']['name']
# # print 'body info', body['share']['size']
# #list 
# # for k in body['services']:
# #     for j in k:
# #         print j, k[j]
# for k in body['services']:
#     # print 'binary', k['binary']
#     # print 'state', k['state']
#     if k['state'] == 'down':
#         # print k
#         print 'down', k['host']
#         print 'down', k['binary']
    # else:
    #     print k

# list
# for _share in body['shares']:
#     print _share['id'], _share['name'], _share['status']
