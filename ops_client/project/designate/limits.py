from ops_client.manager.designate import DesignateBaseManager

class LimitManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/limits", **kwargs)
