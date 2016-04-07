"""
Quotas interface.
"""

from ops_client.manager.nova import NovaBaseManager

class QuotaSetManager(NovaBaseManager):

    def get(self, tenant_id, user_id = None, response_key = True, **kwargs):
        if hasattr(tenant_id, 'tenant_id'):
            tenant_id = tenant_id.tenant_id
        if user_id:
            url = '/os-quota-sets/%s?user_id=%s' % (tenant_id, user_id)
        else:
            url = '/os-quota-sets/%s' % tenant_id

        key = None
        if response_key :
            key = "quota_set"
        return self._get(url, key, **kwargs)

    def _update_body(self, tenant_id, **kwargs):
        kwargs['tenant_id'] = tenant_id
        return {'quota_set': kwargs}

    def update(self, tenant_id, update_body, user_id = None, 
               response_key = True, **kwargs):
        tenant = update_body.get('tenant_id', None)
        if tenant:
            del update_body['tenant_id']
        body = self._update_body(tenant_id, **update_body)
        for key in list(body['quota_set']):
            if body['quota_set'][key] is None:
                body['quota_set'].pop(key)
        if user_id:
            url = '/os-quota-sets/%s?user_id=%s' % (tenant_id, user_id)
        else:
            url = '/os-quota-sets/%s' % tenant_id
        key = None
        if response_key :
            key = "quota_set"
        return self._put(url, body, key, **kwargs)

    def defaults(self, tenant_id, response_key = True, **kwargs):
        key = None
        if response_key :
            key = "quota_set"
        return self._get('/os-quota-sets/%s/defaults' % tenant_id, 
                         key, **kwargs)

    def delete(self, tenant_id, user_id = None, **kwargs):
        if user_id:
            url = '/os-quota-sets/%s?user_id=%s' % (tenant_id, user_id)
        else:
            url = '/os-quota-sets/%s' % tenant_id
        return self._delete(url, **kwargs)
