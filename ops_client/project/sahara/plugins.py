from ops_client.manager.sahara import SaharaBaseManager


class PluginManager(SaharaBaseManager):

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/plugins%s' % query_string
        return self._get(url, **kwargs)

    def get(self, plugin_name, **kwargs):
        url = '/plugins/%s' % plugin_name
        return self._get(url, **kwargs)

    def get_version_details(self, plugin_name, hadoop_version, **kwargs):
        url = '/plugins/%s/%s' % (plugin_name, hadoop_version)
        return self._get(url, **kwargs)

'''
    def convert_to_cluster_template(self, plugin_name, hadoop_version,
                                    template_name, filecontent, **kwargs):
        resp = self.api.post('/plugins/%s/%s/convert-config/%s' %
                             (plugin_name,
                              hadoop_version,
                              urlparse.quote(template_name)),
                             data=filecontent)
        if resp.status_code != 202:
            raise RuntimeError('Failed to upload template file for plugin "%s"'
                               ' and version "%s"' %
                               (plugin_name, hadoop_version))
        else:
            return base.get_json(resp)['cluster_template']
'''
