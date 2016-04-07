from ops_client.manager.designate import DesignateBaseManager

class NameServerManager(DesignateBaseManager):

    def list(self, zone_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/%s/nameservers" % zone_id, **kwargs)
