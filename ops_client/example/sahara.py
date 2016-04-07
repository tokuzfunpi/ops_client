from ops_client.client.sahara import SaharaClient

keystone_url = 'http://10.55.66.133:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'infra_app_LJHRNT'
project_domain = 'default'

_s = SaharaClient(interface='public')

_s.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)


tenant_id = '380bc83ee0bd48a4bcb2d7863b65992c'
user_id = 'be187e41bb2145ab80bdc49e9a501e74'

"""
plugins
"""
plugin_name = 'vanilla'
hadoop_version = '2.7.1'
# resp, body = _s.plugins.list()
# resp, body = _s.plugins.get(plugin_name)
# resp, body = _s.plugins.get_version_details(plugin_name, hadoop_version)
"""
images
"""
image_id = 'ff45b8fb-bcd9-4bf3-bae6-485ed4d13972'
# resp, body = _s.images.list()
# resp, body = _s.images.get(image_id)
# resp, body = _s.images.register_image(image_id, 'ubuntu', 'ttt')
# resp, body = _s.images.unregister_image(image_id)
# resp, body = _s.images.add_tags(image_id, ['vanilla', '2.7.1'])
# resp, body = _s.images.remove_tag(image_id, ['2.7.1'])

"""
node_group_template
"""
master_ng_id = '61a2d8d6-5e09-493f-9bf9-c4c3b64b10c3'
worker_ng_id = 'e19a6693-b09f-4eb5-85cb-6a84564abfe9'

# resp, body = _s.ng_template.list()
# resp, body = _s.ng_template.get(master_ng_id)
# node_processes = [
#     "namenode",
#     "resourcemanager",
#     "oozie",
#     "historyserver"
# ]
# resp, body = _s.ng_template.create('test-master', 'vanilla', '2.7.1', '2',
#                                    node_processes=node_processes)
# node_processes = [
#     "namenode",
#     "resourcemanager"
# ]
# resp, body = _s.ng_template.update(master_ng_id,
#                                    node_processes=node_processes)
# resp, body = _s.ng_template.delete(master_ng_id)

"""
cluster_template
"""
cluster_template_id = '483515e2-35a1-4656-b825-5a04e196067d'
# resp, body = _s.cluster_template.list()
# resp, body = _s.cluster_template.get(cluster_template_id)
# node_groups = [
#     {
#         'name': 'ops_master',
#         'node_group_template_id': master_ng_id,
#         'count': 1
#     },
#     {
#         'name': 'ops_worker',
#         'node_group_template_id': worker_ng_id,
#         'count': 2
#     }
# ]
# resp, body = _s.cluster_template.create('test-cluster', 'vanilla', '2.7.1',
#                                         node_groups=node_groups)
# node_groups = [
#     {
#         'name': 'ops-worker2',
#         'node_group_template_id': worker_ng_id,
#         'count': 1
#     }
# ]
# resp, body = _s.cluster_template.update(cluster_template_id,
#                                         node_groups=node_groups)
# resp, body = _s.cluster_template.delete(cluster_template_id)

"""
cluster
"""
cluster_id = '19cd3297-d397-41db-94fa-64cba7055bbd'
image_id = 'ff45b8fb-bcd9-4bf3-bae6-485ed4d13972'
net_id = 'cdd4ffc7-64db-4bf9-8170-d95796167419'
keypair = 'vanilla'
# resp, body = _s.clusters.list()
# resp, body = _s.clusters.create('test-cluster', 'vanilla', '2.7.1',
#                                 cluster_template_id=cluster_template_id,
#                                 default_image_id=image_id,
#                                 user_keypair_id=keypair,
#                                 net_id=net_id,
#                                 count=2)
# resp, body = _s.clusters.get(cluster_id)
# resp, body = _s.clusters.update(cluster_id, is_public=True)
# scale_object = {
#     'resize_node_groups': [
#         {
#             'count': 4,
#             'name': 'worker-node'
#         }
#     ]
# }
# resp, body = _s.clusters.scale(cluster_id, scale_object)
# resp, body = _s.clusters.delete(cluster_id)

"""
data-sources
"""
data_source_id = '17b96819-4538-4fb3-aaa0-21f14b8e60b6'
# resp, body = _s.data_sources.list()
# resp, body = _s.data_sources.create(
#     'test-in', 'manila',
#     'manila://843b3ec3-c7fd-4205-9ffc-f1b18da38c20/input.txt')
# resp, body = _s.data_sources.get(data_source_id)
# update_data = {
#     'description': 'aaaaaaa'
# }
# resp, body = _s.data_sources.update(data_source_id, update_data)
# resp, body = _s.data_sources.delete(data_source_id)

"""
job-binaries
"""
job_binary_id = '6d9d389b-361d-48e0-af46-e04e3669b3ce'
manila = 'manila://08507603-af8a-42f4-bc6b-6027a8322cbd'
jar = '/hadoop-mapreduce-examples-2.6.0.jar'
# resp, body = _s.job_binaries.list()
# resp, body = _s.job_binaries.create(
#     'test-input',
#     manila + jar)
# resp, body = _s.job_binaries.get(job_binary_id)
# data = {
#     "url": manila + jar
# }
# resp, body = _s.job_binaries.update(job_binary_id, data)
# resp, body = _s.job_binaries.get_file(job_binary_id)  # error
# resp, body = _s.job_binaries.delete(job_binary_id)

"""
job-types
"""
# resp, body = _s.job_types.list()

"""
jobs
"""
job_id = 'c33a5b02-b5e1-4c95-9db1-b40e1caff173'
# resp, body = _s.jobs.list()
# resp, body = _s.jobs.create('test-job', 'Java', libs=[job_binary_id])
# resp, body = _s.jobs.get(job_id)
# resp, body = _s.jobs.get_configs('Java')
# resp, body = _s.jobs.update(job_id, description='aaa')
# resp, body = _s.jobs.delete(job_id)

"""
job-executions
"""
job_execute_id = '92b3b698-4514-4cec-a1ce-c16a91124715'
# resp, body = _s.job_executions.list()
configs = {
    "configs": {
        "mapred.map.tasks": "1",
        "mapred.reduce.tasks": "1",
        "edp.java.main_class": "org.apache.hadoop.examples.WordCount"
    },
    "args": [
        "file:///mnt/843b3ec3-c7fd-4205-9ffc-f1b18da38c20/input.txt",
        "file:///home/hadoop/output"
    ]
}
# resp, body = _s.job_executions.create(job_id, cluster_id, configs)
# resp, body = _s.job_executions.get(job_execute_id)
# resp, body = _s.job_executions.update(job_execute_id, is_public=True)
# resp, body = _s.job_executions.delete(job_execute_id)
# resp, body = _s.job_executions.cancel(job_execute_id)
# resp, body = _s.job_executions.refresh_status(job_execute_id)

"""
job-binary-internals
"""
job_binary_int_id = '1137a380-b91e-4549-b599-dfcc9a47b820'
file_path = '/home/vianna/wrk/openstack/sahara/etc/edp-examples/' + \
            'hadoop2/edp-java/hadoop-mapreduce-examples-2.6.0.jar'
# upload_file = open(file_path, 'rb')
# resp, body = _s.job_binary_int.list()
# resp, body = _s.job_binary_int.create('test.jar', upload_file)
# upload_file.close()
# resp, body = _s.job_binary_int.get(job_binary_int_id)
# resp, body = _s.job_binary_int.update(job_binary_int_id, is_public=True)
# resp, body = _s.job_binary_int.delete(job_binary_int_id)
# resp, body = _s.job_binary_int.get_file(job_binary_int_id)

print resp
print body
