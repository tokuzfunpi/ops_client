from ops_client.manager.ceilometer import CeilometerBaseManager

class TraitDescriptionManager(CeilometerBaseManager):

    def list(self, event_type, **kwargs):
        path = '/event_types/%s/traits' % event_type
        return self._get(path, **kwargs)