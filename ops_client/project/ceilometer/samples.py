from ops_client.manager.ceilometer import CeilometerBaseManager

CREATION_ATTRIBUTES = ('source',
                       'counter_name',
                       'counter_type',
                       'counter_unit',
                       'counter_volume',
                       'user_id',
                       'project_id',
                       'resource_id',
                       'timestamp',
                       'resource_metadata')

class SampleManager(CeilometerBaseManager):

    @staticmethod
    def _path(counter_name=None):
        return '/meters/%s' % counter_name if counter_name else '/meters'

    def list(self, meter_name=None, q=None, limit=None, **kwargs):
        url = self._path(counter_name=meter_name)
        params = ['limit=%s' % str(limit)] if limit else None
        path = self.build_url(url, q, params)
        return self._get(path, **kwargs)

    def create(self, counter_name, body_list, **kwargs):
        new_list = []
        for _body in body_list:
            _new = dict((key, value) for (key, value) in _body.items()
                         if key in CREATION_ATTRIBUTES)
            new_list.append(_new)
        url = self._path(counter_name=counter_name)
        return self._post(url, new_list, **kwargs)