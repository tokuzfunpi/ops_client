from ops_client.manager.cinder import CinderBaseManager

class QuotaSetManager(CinderBaseManager):

    def get(self, tenant_id, usage=False, **kwargs):
        return self._get("/os-quota-sets/%s?usage=%s" % (tenant_id, usage), 
                         **kwargs)

    def update(self, tenant_id, updates = None, **kwargs):
        body = {'quota_set': {'tenant_id': tenant_id}}

        if not updates:
            return

        for update in updates:
            body['quota_set'][update] = updates[update]

        return self._put('/os-quota-sets/%s' % (tenant_id), body = body, 
                         **kwargs)

    def defaults(self, tenant_id, **kwargs):
        return self._get('/os-quota-sets/%s/defaults' % tenant_id, **kwargs)

    def delete(self, tenant_id, **kwargs):
        return self._delete("/os-quota-sets/%s" % tenant_id, **kwargs)
