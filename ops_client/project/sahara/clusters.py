from six.moves.urllib import parse
from ops_client.manager.sahara import SaharaBaseManager


class ClusterManager(SaharaBaseManager):

    def create(self, name, plugin_name, hadoop_version,
               cluster_template_id=None, default_image_id=None,
               is_transient=None, description=None, cluster_configs=None,
               node_groups=None, user_keypair_id=None,
               anti_affinity=None, net_id=None, count=None,
               use_autoconfig=None, shares=None,
               is_public=None, is_protected=None, **kwargs):

        data = {
            'name': name,
            'plugin_name': plugin_name,
            'hadoop_version': hadoop_version,
        }

        # Checking if count is greater than 1, otherwise we set it to None
        # so the created dict in the _copy_if_defined method does not contain
        # the count parameter.
        if count and count <= 1:
            count = None

        self._copy_if_defined(data,
                              cluster_template_id=cluster_template_id,
                              is_transient=is_transient,
                              default_image_id=default_image_id,
                              description=description,
                              cluster_configs=cluster_configs,
                              node_groups=node_groups,
                              user_keypair_id=user_keypair_id,
                              anti_affinity=anti_affinity,
                              neutron_management_network=net_id,
                              count=count,
                              use_autoconfig=use_autoconfig,
                              shares=shares,
                              is_public=is_public,
                              is_protected=is_protected)
        if count:
            url = '/clusters/multiple'
        else:
            url = '/clusters'

        return self._post(url, data, **kwargs)

    def scale(self, cluster_id, scale_object, **kwargs):
        return self._put('/clusters/%s' % cluster_id, scale_object, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/clusters%s' % query_string
        return self._get(url, **kwargs)

    def get(self, cluster_id, show_progress=False, **kwargs):
        url = ('/clusters/%(cluster_id)s?%(params)s' %
               {"cluster_id": cluster_id,
                "params": parse.urlencode({"show_progress": show_progress})})

        return self._get(url, **kwargs)

    def delete(self, cluster_id, **kwargs):
        url = '/clusters/%s' % cluster_id
        return self._delete(url, **kwargs)

    def update(self, cluster_id, name=None, description=None, is_public=None,
               is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(data, name=name, description=description,
                              is_public=is_public, is_protected=is_protected)

        url = '/clusters/%s' % cluster_id
        return self._patch(url, data, **kwargs)
