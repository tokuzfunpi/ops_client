from ops_client.client.glance import GlanceClient

keystone_url = 'http://10.55.66.103:5000'
user_name = 'admin'
user_pwd = 'admin'
user_domain = 'default'
project_name = 'admin'
project_domain = 'default'

_g = GlanceClient(interface='public')

_g.authenticate(keystone_url, user_name=user_name, user_pwd=user_pwd,
                user_domain=user_domain, project_name=project_name,
                project_domain=project_domain)

# upload_file = open('/cirros-0.3.3-x86_64-disk.img','rb')
upload_file = open('/ubuntu-12.04.5-server-amd64.iso', 'rb')

"""
test_image:
"""
# img_id = 'c90a8173-2c10-416b-89f3-daa545765a03'
# resp, body = _g.images.list()
# resp, body = _g.images.get(img_id)
# resp, body = _g.images.data(img_id)
# resp, body = _g.images.create(image_name = "ubuntu",
#                               image_type = 'image_type',
#                               disk_format = "qcow2",
#                               container_format = "bare")
# img_id = body['id']
# body = _g.images.update(img_id,
#                         [{"op":"add", "path":"/sound_driver","value":"ac97"}])
# resp, body = _g.images.upload(img_id, upload_file)
# resp, body = _g.images.delete(img_id)
# not test location part
# resp, body = _g.images.add_location(img_id,
#                                     'http://test.com/test.test',{'aa':'aaa'})
# (not test)

"""
test_schema:
"""
# resp, body = _g.schema.get('image')
# resp, body = _g.schema.get('images')

"""
test_image_tag:
"""
# resp, body = _g.image_tags.update(img_id, 'test')
# resp, body = _g.image_tags.delete(img_id, 'test')

"""
test_image_member:
"""
admin_id = ''
# resp, body = _g.image_members.list(img_id)
# resp, body = _g.image_members.create(img_id, admin_id)
# resp, body = _g.image_members.update(img_id, admin_id, 'accepted')
# resp, body = _g.image_members.delete(img_id, admin_id)

"""
test_metadef_ns:
"""
namespace = ''
# resp, body = _g.metadef_ns.list(page_size = 1)
# resp, body = _g.metadef_ns.get(namespace,
#     query = {'resource_type':'OS::Nova::Flavor'})
# resp, body = _g.metadef_ns.create('bbb', extra_body = {"description":"kk"})
# resp, body = _g.metadef_ns.update(namespace, 'vvv'
#     extra_body = {"description":"vvvvvv"})
# resp, body = _g.metadef_ns.delete(namespace)

"""
test_metadef_rt:
"""
res_type = ''
# resp, body = _g.metadef_rt.list()
# resp, body = _g.metadef_rt.get(namespace)
# resp, body = _g.metadef_rt.associate(namespace,
#     res_type = {'name': 'OS::Glance::Image'})
# resp, body = _g.metadef_rt.deassociate(namespace, res_type)

"""
test_metadef_prop:
"""
prop = ''
# resp, body = _g.metadef_prop.list(namespace)
# resp, body = _g.metadef_prop.create(namespace, 'bbb', 'AAA', 'string',
#     extra_body = {"description": "GGGG"})
# resp, body = _g.metadef_prop.get(namespace, prop)
# resp, body = _g.metadef_prop.update(namespace, prop, 'aaa', 'AAA', 'string',
#         extra_body = {"description":"DFSDGSDGSDG"})
# resp, body = _g.metadef_prop.delete(namespace, prop)
# resp, body = _g.metadef_prop.delete_all(namespace)

"""
test_metadef_obj:
"""
obj = ''
# resp, body = _g.metadef_obj.list(namespace)
# resp, body = _g.metadef_obj.create(namespace, 'ttt')
# resp, body = _g.metadef_obj.update(namespace, obj, 'obj',
#     extra_body = {'description':'asdfad'})
# resp, body = _g.metadef_obj.get(namespace, obj)
# resp, body = _g.metadef_obj.delete(namespace, obj)
# resp, body = _g.metadef_obj.delete_all(namespace)

print 'resp = ',resp
print 'body = ',body
