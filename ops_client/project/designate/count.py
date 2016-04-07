from ops_client.manager.designate import DesignateBaseManager

class CountManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/reports/counts", **kwargs)

    def show(self, criterion, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        if criterion == 'zones':
            criterion = 'domains'
        return self._get(prefix+"/reports/counts/%s" % criterion, **kwargs)
