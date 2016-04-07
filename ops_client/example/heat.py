from ops_client.client.heat import HeatClient

keystone_url = 'http://10.55.66.105:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_h = HeatClient(interface='public')

_h.authenticate(keystone_url,
                user_name=user_name,
                user_pwd=user_pwd,
                user_domain=user_domain,
                project_name=project_name,
                project_domain=project_domain)

'''
test_stack
'''
stack_name = 'test3'
stack_id = 'bd933819-b4ca-46a9-a939-fe38a12e5dd8'
template = {
    "heat_template_version": "2013-05-23",
    "description": "test",
    "parameters": {
        "flavor": {
            "default": "m1.small",
            "type": "string"
        }
    },
    "resources": {
        "hello_world": {
            "type": "OS::Nova::Server",
            "properties": {
                "flavor": {
                    "get_param": "flavor"
                },
                "image": "bcf3242e-8ee6-4aea-929d-f2c2e30180f2",
                "networks": [
                    {
                        "uuid": "a816fa2f-8cc5-48e2-959e-fdcdbfc21bcd"
                    }
                ],
                "user_data": "#!/bin/bash -xv\necho \"hello world\" &gt; /root/hello-world.txt\n"
            }
        }
    }
}
extra_body = {
    "heat_template_version": "2013-05-23",
    "description": "test2",
    "parameters": {
        "flavor": {
            "default": "m1.small",
            "type": "string"}
        },
        "resources": {
            "hello_world": {
                "type": "OS::Nova::Server",
                "properties": {
                    "flavor": {
                        "get_param": "flavor"
                    },
                    "image": "bcf3242e-8ee6-4aea-929d-f2c2e30180f2",
                    "networks": [
                        {
                            "uuid": "a816fa2f-8cc5-48e2-959e-fdcdbfc21bcd"
                        }
                    ],
                    "user_data": "#!/bin/bash -xv\necho \"hello world\" &gt; /root/hello-world.txt\n"
                }
            }
        }
    }
resp, body = _h.stacks.list()
# resp, body = _h.stacks.create('test3', template=template)
# resp, body = _h.stacks.preview('test1', template=template)
# resp, body = _h.stacks.get(stack_name, stack_id)
# resp, body = _h.stacks.delete(stack_name, stack_id)
# resp, body = _h.stacks.abandon(stack_name, stack_id)
# resp, body = _h.stacks.update(stack_name, stack_id, template=extra_body)
# resp, body = _h.stacks.preview_update(stack_name, stack_id, template=extra_body)

'''
test_build_info
'''
# resp, body = _h.build_info.get()

'''
test_events
'''
resource_name = 'hello_world'
event_id = '6bb2e0f1-216f-4364-9de4-9bebb6c329dd'
# resp, body = _h.events.list(stack_name, stack_id)
# resp, body = _h.events.list(stack_name, stack_id, resource_name=resource_name)
# resp, body = _h.events.get(stack_name, stack_id, resource_name, event_id)

'''
test_resource_types
'''
resource_type = 'OS::Nova::Flavor'
# resp, body = _h.resource_types.list()
# resp, body = _h.resource_types.get(resource_type)
# resp, body = _h.resource_types.get_template(resource_type, template_type='cfn')
# resp, body = _h.resource_types.get_template(resource_type)

'''
test_resources
'''
# resp, body = _h.resources.list(stack_name, stack_id)
# resp, body = _h.resources.get(stack_name, stack_id, resource_name)
# resp, body = _h.resources.metadata(stack_name, stack_id, resource_name)
# resp, body = _h.resources.signal(stack_name, stack_id, resource_name)

'''
test_services
'''
# resp, body = _h.services.list()

'''
test_snapshots
'''
snapshot_id = '20002489-3728-45a1-b5d7-ddc806a9a2e9'
# resp, body = _h.snapshots.list(stack_name, stack_id)
# resp, body = _h.snapshots.create(stack_name, stack_id)
# resp, body = _h.snapshots.get(stack_name, stack_id, snapshot_id)
# resp, body = _h.snapshots.restore(stack_name, stack_id, snapshot_id)
# resp, body = _h.snapshots.delete(stack_name, stack_id, snapshot_id)

'''
test_software_configs
'''
config_id = '1538ddaa-9408-4e59-893c-62e05d98bf97'
inputs = [
    {
        "default": None,
        "type": "string",
        "name": "test_input",
        "description": "ttttt"
    }
]
# resp, body = _h.software_configs.create(inputs=inputs)
# resp, body = _h.software_configs.get(config_id)
# resp, body = _h.software_configs.delete(config_id)

'''
test_software_deployments
'''
server_id = '917316a3-76e4-437f-a330-2d2c28fd954d'
deployment_id = 'bdd05911-7798-4d38-bbfd-e743b0ad899b'
extra_body = {
    "input": server_id
}
# resp, body = _h.software_deployments.list()
# resp, body = _h.software_deployments.metadata(server_id)
# resp, body = _h.software_deployments.create(config_id, server_id, 'CREATE')
# resp, body = _h.software_deployments.get(deployment_id) # will raise error if deployment had been updated as status='IN_PROGRESS'
# resp, body = _h.software_deployments.update(deployment_id, status='COMPLETE')
# resp, body = _h.software_deployments.delete(deployment_id)

'''
test_stack_actions
'''
# resp, body = _h.stack_actions.check(stack_name, stack_id)
# resp, body = _h.stack_actions.suspend(stack_name, stack_id)
# resp, body = _h.stack_actions.resume(stack_name, stack_id)
# resp, body = _h.stack_actions.cancel_update(stack_name, stack_id)

'''
test_template_versions
'''
template_version = 'heat_template_version.2014-10-16'
# resp, body = _h.template_versions.list()
# resp, body = _h.template_versions.get(template_version)

'''
test_templates
'''
# resp, body = _h.templates.get(stack_name, stack_id)
# resp, body = _h.templates.validate()

print resp
print body