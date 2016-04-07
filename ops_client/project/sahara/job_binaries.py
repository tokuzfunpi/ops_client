from ops_client.manager.sahara import SaharaBaseManager


class JobBinaryManager(SaharaBaseManager):

    def create(self, name, url, description='', extra={}, is_public=None,
               is_protected=None, **kwargs):
        data = {
            "name": name,
            "url": url,
            "description": description,
            "extra": extra
        }

        self._copy_if_defined(data, is_public=is_public,
                              is_protected=is_protected)
        url = '/job-binaries'
        return self._post(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/job-binaries%s' % query_string
        return self._get(url, **kwargs)

    def get(self, job_binary_id, **kwargs):
        url = '/job-binaries/%s' % job_binary_id
        return self._get(url, **kwargs)

    def delete(self, job_binary_id, **kwargs):
        url = '/job-binaries/%s' % job_binary_id
        return self._delete(url, **kwargs)

    def get_file(self, job_binary_id, **kwargs):
        url = '/job-binaries/%s/data' % job_binary_id
        return self._get(url, **kwargs)

    def update(self, job_binary_id, data, **kwargs):
        url = '/job-binaries/%s' % job_binary_id
        return self._put(url, data, **kwargs)
