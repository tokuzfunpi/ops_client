from ops_client.manager.designate import DesignateBaseManager

class QuotaManager(DesignateBaseManager):

    def show(self, quota_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/quotas/%s" % quota_id, **kwargs)

    def update(self, quota_id, zones = None, zone_records = None,
               update_body = {}, prefix='', **kwargs):
        body = {}
        if zones:
            body['domains'] = zones
        if zone_records:
            body['domain_records'] = zone_records
        # use update_body for creep-client.
        if update_body:
            body.update(update_body)
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._put(prefix+"/quotas/%s" % quota_id, body = body, **kwargs)

    def delete(self, quota_id, prefix='', **kwargs):
        return self._delete(prefix+'/quotas/%s' % quota_id, **kwargs)
