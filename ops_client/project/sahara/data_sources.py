from ops_client.manager.sahara import SaharaBaseManager


class DataSourceManager(SaharaBaseManager):

    def create(self, name, data_source_type, url,
               description='', credential_user=None, credential_pass=None,
               is_public=None, is_protected=None, **kwargs):
        data = {
            'name': name,
            'description': description,
            'type': data_source_type,
            'url': url,
            'credentials': {}
        }
        self._copy_if_defined(data['credentials'],
                              user=credential_user,
                              password=credential_pass)

        self._copy_if_defined(data, is_public=is_public,
                              is_protected=is_protected)

        url = '/data-sources'
        return self._post(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/data-sources%s' % query_string
        return self._get(url, **kwargs)

    def get(self, data_source_id, **kwargs):
        url = '/data-sources/%s' % data_source_id
        return self._get(url, **kwargs)

    def delete(self, data_source_id, **kwargs):
        url = '/data-sources/%s' % data_source_id
        return self._delete(url, **kwargs)

    def update(self, data_source_id, update_data, **kwargs):
        url = '/data-sources/%s' % data_source_id
        return self._put(url, update_data, **kwargs)
