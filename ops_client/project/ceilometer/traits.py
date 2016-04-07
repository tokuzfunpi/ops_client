from ops_client.manager.ceilometer import CeilometerBaseManager

class TraitManager(CeilometerBaseManager):

    def list(self, event_type, trait_name, **kwargs):
        path = '/event_types/%s/traits/%s' % (event_type, trait_name)
        return self._get(path, **kwargs)
