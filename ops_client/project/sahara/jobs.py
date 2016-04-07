from ops_client.manager.sahara import SaharaBaseManager


class JobManager(SaharaBaseManager):

    def create(self, name, job_type, mains=[], libs=[], description='',
               interface=None, is_public=None, is_protected=None, **kwargs):
        data = {
            'name': name,
            'type': job_type,
            'description': description,
            'mains': mains,
            'libs': libs,
        }

        self._copy_if_defined(data, interface=interface, is_public=is_public,
                              is_protected=is_protected)
        url = '/jobs'

        return self._post(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/jobs%s' % query_string
        return self._get(url, **kwargs)

    def get(self, job_id, **kwargs):
        url = '/jobs/%s' % job_id
        return self._get(url, **kwargs)

    def get_configs(self, job_type, **kwargs):
        url = '/jobs/config-hints/%s' % job_type
        return self._get(url, **kwargs)

    def delete(self, job_id, **kwargs):
        url = '/jobs/%s' % job_id
        return self._delete(url, **kwargs)

    def update(self, job_id, name=None, description=None, is_public=None,
               is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(data, name=name, description=description,
                              is_public=is_public, is_protected=is_protected)

        url = '/jobs/%s' % job_id
        return self._patch(url, data, **kwargs)
