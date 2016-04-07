import six
from six.moves.urllib import parse
from ops_client.manager.sahara import SaharaBaseManager


class NodeGroupTemplateManager(SaharaBaseManager):

    def create(self, name, plugin_name, hadoop_version, flavor_id,
               description=None, volumes_per_node=None, volumes_size=None,
               node_processes=None, node_configs=None, floating_ip_pool=None,
               security_groups=None, auto_security_group=None,
               availability_zone=None, volumes_availability_zone=None,
               volume_type=None, image_id=None, is_proxy_gateway=None,
               volume_local_to_instance=None, use_autoconfig=None,
               shares=None, is_public=None, is_protected=None, **kwargs):

        data = {
            'name': name,
            'plugin_name': plugin_name,
            'hadoop_version': hadoop_version,
            'flavor_id': flavor_id,
            'node_processes': node_processes
        }

        self._copy_if_defined(data,
                              description=description,
                              node_configs=node_configs,
                              floating_ip_pool=floating_ip_pool,
                              security_groups=security_groups,
                              auto_security_group=auto_security_group,
                              availability_zone=availability_zone,
                              image_id=image_id,
                              is_proxy_gateway=is_proxy_gateway,
                              use_autoconfig=use_autoconfig,
                              shares=shares,
                              is_public=is_public,
                              is_protected=is_protected
                              )

        if volumes_per_node:
            data.update({"volumes_per_node": volumes_per_node,
                         "volumes_size": volumes_size})
            if volumes_availability_zone:
                data.update({"volumes_availability_zone":
                             volumes_availability_zone})
            if volume_type:
                data.update({"volume_type": volume_type})
            if volume_local_to_instance:
                data.update(
                    {"volume_local_to_instance": volume_local_to_instance})
        url = '/node-group-templates'

        return self._post(url, data, **kwargs)

    def update(self, ng_template_id, name=None, plugin_name=None,
               hadoop_version=None, flavor_id=None, description=None,
               volumes_per_node=None, volumes_size=None, node_processes=None,
               node_configs=None, floating_ip_pool=None, security_groups=None,
               auto_security_group=None, availability_zone=None,
               volumes_availability_zone=None, volume_type=None,
               image_id=None, is_proxy_gateway=None,
               volume_local_to_instance=None, use_autoconfig=None,
               shares=None, is_public=None, is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(
            data, name=name, plugin_name=plugin_name,
            hadoop_version=hadoop_version, flavor_id=flavor_id,
            description=description, volumes_per_node=volumes_per_node,
            volumes_size=volumes_size, node_processes=node_processes,
            node_configs=node_configs, floating_ip_pool=floating_ip_pool,
            security_groups=security_groups,
            auto_security_group=auto_security_group,
            availability_zone=availability_zone,
            volumes_availability_zone=volumes_availability_zone,
            volume_type=volume_type, image_id=image_id,
            is_proxy_gateway=is_proxy_gateway,
            volume_local_to_instance=volume_local_to_instance,
            use_autoconfig=use_autoconfig, shares=shares,
            is_public=is_public, is_protected=is_protected
        )
        url = '/node-group-templates/%s' % ng_template_id

        return self._put(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/node-group-templates%s' % query_string
        return self._get(url, **kwargs)

    def get(self, ng_template_id, **kwargs):
        url = '/node-group-templates/%s' % ng_template_id
        return self._get(url, **kwargs)

    def delete(self, ng_template_id, **kwargs):
        url = '/node-group-templates/%s' % ng_template_id
        return self._delete(url, **kwargs)
