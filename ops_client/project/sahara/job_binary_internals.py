from six.moves.urllib import parse
from ops_client.manager.sahara import SaharaBaseManager


class JobBinaryInternalManager(SaharaBaseManager):

    def create(self, name, data, **kwargs):
        url = '/job-binary-internals/%s' % parse.quote(name.encode('utf-8'))
        return self._put(url, data, **kwargs)

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/job-binary-internals%s' % query_string
        return self._get(url, **kwargs)

    def get(self, job_binary_id, **kwargs):
        url = '/job-binary-internals/%s' % job_binary_id
        return self._get(url, **kwargs)

    def delete(self, job_binary_id, **kwargs):
        url = '/job-binary-internals/%s' % job_binary_id
        return self._delete(url, **kwargs)

    def update(self, job_binary_id, name=None, is_public=None,
               is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(data, name=name, is_public=is_public,
                              is_protected=is_protected)

        url = '/job-binary-internals/%s' % job_binary_id
        return self._patch(url, data, **kwargs)

    def get_file(self, job_binary_id, **kwargs):
        url = '/job-binary-internals/%s/data' % job_binary_id
        return self._get(url, **kwargs)
