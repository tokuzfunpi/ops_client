from ops_client.manager.manila import ManilaBaseManager


class QuotaSetManager(ManilaBaseManager):

    def get(self, tenant_id, user_id=None, **kwargs):
        if hasattr(tenant_id, 'tenant_id'):
            tenant_id = tenant_id.tenant_id
        if user_id:
            url = "/os-quota-sets/%s?user_id=%s" % (tenant_id, user_id)
        else:
            url = "/os-quota-sets/%s" % tenant_id
        return self._get(url, **kwargs)

    def update(self, tenant_id, shares=None, snapshots=None,
               gigabytes=None, snapshot_gigabytes=None,
               share_networks=None, force=None, user_id=None, **kwargs):
        body = {
            'quota_set': {
                'tenant_id': tenant_id,
                'shares': shares,
                'snapshots': snapshots,
                'gigabytes': gigabytes,
                'snapshot_gigabytes': snapshot_gigabytes,
                'share_networks': share_networks,
                'force': force,
            }
        }

        for key in list(body['quota_set']):
            if body['quota_set'][key] is None:
                body['quota_set'].pop(key)
        if user_id:
            url = '/os-quota-sets/%s?user_id=%s' % (tenant_id, user_id)
        else:
            url = '/os-quota-sets/%s' % tenant_id

        return self._put(url, body, **kwargs)

    def defaults(self, tenant_id, **kwargs):
        return self._get('/os-quota-sets/%s/defaults' % tenant_id, **kwargs)

    def delete(self, tenant_id, user_id=None, **kwargs):
        if user_id:
            url = '/os-quota-sets/%s?user_id=%s' % (tenant_id, user_id)
        else:
            url = '/os-quota-sets/%s' % tenant_id
        return self._delete(url, **kwargs)
