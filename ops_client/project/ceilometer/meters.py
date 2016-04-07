from ops_client.manager.ceilometer import CeilometerBaseManager

class MeterManager(CeilometerBaseManager):

    def list(self, q = None, **kwargs):
        path = self.build_url('/meters', q)
        return self._get(path, **kwargs)