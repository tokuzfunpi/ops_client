from ops_client.manager.ceilometer import CeilometerBaseManager

class EventManager(CeilometerBaseManager):

    def list(self, q = None, **kwargs):
        path = self.build_url('/events', q)
        return self._get(path, **kwargs)

    def get(self, message_id, **kwargs):
        path = '/events/%s'
        try:
            return self._get('/events/%s' % message_id,
                             expect_single=True, **kwargs)
        except IndexError:
            return None
