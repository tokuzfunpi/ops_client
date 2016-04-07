from ops_client.manager.ceilometer import CeilometerBaseManager

class ResourceManager(CeilometerBaseManager):

    def list(self, q = None, **kwargs):
        path = self.build_url('/resources', q)
        return self._get(path, **kwargs)

    def get(self, resource_id, **kwargs):
        path = '/resources/%s' % resource_id
        try:
            return self._get(path, expect_single=True, **kwargs)
        except IndexError:
            return None