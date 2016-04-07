import six
from six.moves.urllib import parse
from ops_client.manager.sahara import SaharaBaseManager


class ClusterTemplateManager(SaharaBaseManager):

    def create(self, name, plugin_name, hadoop_version, description=None,
               cluster_configs=None, node_groups=None, anti_affinity=None,
               net_id=None, default_image_id=None, use_autoconfig=None,
               shares=None, is_public=None, is_protected=None, **kwargs):

        data = {
            'name': name,
            'plugin_name': plugin_name,
            'hadoop_version': hadoop_version,
        }

        self._copy_if_defined(data,
                              description=description,
                              cluster_configs=cluster_configs,
                              node_groups=node_groups,
                              anti_affinity=anti_affinity,
                              neutron_management_network=net_id,
                              default_image_id=default_image_id,
                              use_autoconfig=use_autoconfig,
                              shares=shares,
                              is_public=is_public,
                              is_protected=is_protected)
        url = '/cluster-templates'

        return self._post(url, data, **kwargs)

    def update(self, cluster_template_id, name=None, plugin_name=None,
               hadoop_version=None, description=None, cluster_configs=None,
               node_groups=None, anti_affinity=None, net_id=None,
               default_image_id=None, use_autoconfig=None, shares=None,
               is_public=None, is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(data, name=name,
                              plugin_name=plugin_name,
                              hadoop_version=hadoop_version,
                              description=description,
                              cluster_configs=cluster_configs,
                              node_groups=node_groups,
                              anti_affinity=anti_affinity,
                              neutron_management_network=net_id,
                              default_image_id=default_image_id,
                              use_autoconfig=use_autoconfig,
                              shares=shares,
                              is_public=is_public,
                              is_protected=is_protected)
        url = '/cluster-templates/%s' % cluster_template_id

        return self._put(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/cluster-templates%s' % query_string
        return self._get(url, **kwargs)

    def get(self, cluster_template_id, **kwargs):
        url = '/cluster-templates/%s' % cluster_template_id
        return self._get(url, **kwargs)

    def delete(self, cluster_template_id, **kwargs):
        url = '/cluster-templates/%s' % cluster_template_id
        return self._delete(url, **kwargs)
