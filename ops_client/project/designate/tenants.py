from ops_client.manager.designate import DesignateBaseManager

class TenantManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/reports/tenants", **kwargs)

    def show(self, tenant_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/reports/tenants/%s" % tenant_id, **kwargs)
