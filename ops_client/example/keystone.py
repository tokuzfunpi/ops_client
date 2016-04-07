from ops_client.client.keystone import KeystoneClient

keystone_url =  'http://10.55.66.84:5000'
user_name = 'admin' 
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin' 
project_domain_name = 'default'

_k = KeystoneClient(interface = 'public')

_k.authenticate(keystone_url, user_name, user_pwd, user_domain,
                project_name, project_domain_name)

"""
NEED TO SET KEYSTONE ENDPOINT TO v3.
"""


"""
test_credential (Not test):
"""
user_id = ''
# resp, body = _k.credentials.create_credential(user_id, "aaa", "bbb")
# resp, body = _k.credentials.create_credential(user_id,
#                                               "aaa",
#                                               data={"blob":{"bbb":"b1"}})
# resp, body = _k.credentials.get_credential(credential_id)
# resp, body = _k.credentials.list_credential()
# resp, body = _k.credentials.update_credential(credential_id,
#                                               user_id,
#                                               project_id=project_id)
# resp, body = _k.credentials.delete_credential(credential_id)

"""
test_group:
"""
group_id = ''
# resp, body = _k.groups.create_group('admin')
# resp, body = _k.groups.list_group()
# resp, body = _k.groups.get_group(group_id)
# resp, body = _k.groups.update_group(group_id, description="admin group")
# resp, body = _k.groups.delete_group(group_id)


"""
test_user:
"""
user_id = ''
# resp, body = _k.users.create_user("test")
# resp, body = _k.users.get_user(user_id)
# resp, body = _k.users.list_user()
# resp, body = _k.users.update_user(user_id, password = 'user')
# resp, body = _k.users.add_to_group(user_id, group_id)
# resp, body = _k.users.check_in_group(user_id, group_id)
# resp, body = _k.users.remove_from_group(user_id, group_id)
# resp, body = _k.users.delete_user(user_id)


"""
test_domain:
"""
domain_id = ''
# resp, body = _k.domains.create_domain("test")
# resp, body = _k.domains.get_domain(domain_id)
# resp, body = _k.domains.list_domain()
# resp, body = _k.domains.update_domain(domain_id, enabled=False)
# resp, body = _k.domains.delete_domain(domain_id)

"""
test_project:
"""
project_id = ''
# resp, body = _k.projects.create_project('test',domain_id)
# resp, body = _k.projects.list_project(user_id)
# resp, body = _k.projects.get_project(project_id)
# resp, body = _k.projects.update_project(project_id, description="test project")
# resp, body = _k.projects.delete_project(project_id)

"""
test_service:
"""
service_id = ''
# resp, body = _k.services.create_service("test_name","test_type")
# resp, body = _k.services.get_service(service_id)
# resp, body = _k.services.update_service(service_id,type="update type")
# resp, body = _k.services.delete_service(service_id)

"""
test_endpoint:
"""
endpoint_id = ''
# resp, body = _k.endpoints.create_endpoint(service_id,
#                                           'http://123.123.123.123:5678',
#                                           interface='public')
# resp, body = _k.endpoints.get_endpoint(endpoint_id)
# resp, body = _k.endpoints.list_endpoint(service_id=service_id)
# resp, body = _k.endpoints.update_endpoint(endpoint_id, interface='internal')
# (only can use 'public/admin/internal')
# resp, body = _k.endpoints.delete_endpoint(endpoint_id)

"""
test_policy (Not test):
"""
# resp, body = _k.policies.create_policy({"aaa":"aaa"})
# resp, body = _k.policies.get_policy(policy_id)
# resp, body = _k.policies.list_policy()
# resp, body = _k.policies.update_policy(policy_id, type='kkk')
# resp, body = _k.policies.delete_policy(policy_id)

"""
test_role:
"""
role_id = ''
# resp, body = _k.roles.create_role("test")
# resp, body = _k.roles.get_role(role_id)
# resp, body = _k.roles.list_role()
# resp, body = _k.roles.update_role(role_id,name="update role")
# resp, body = _k.roles.grant_role(role_id,user_id=user_id,project_id=project_id)
# resp, body = _k.roles.check_role(role_id,project_id=project_id,user_id=user_id)
# resp, body = _k.roles.revoke(role_id,project_id=project_id,user_id=user_id)
# resp, body = _k.roles.delete_role(role_id)

print 'resp = ',resp
print 'body = ',body
