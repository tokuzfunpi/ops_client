from ops_client.manager.neutron import NeutronBaseManager

class QuotaManager(NeutronBaseManager):

    # def get_quotas_tenant(self, params = None, **kwargs):
    #     """Fetch tenant info in server's context for
    #     following quota operation.
    #     """
    #     return self._get(self.quota_path % 'tenant', params=params, **kwargs)

    def list_quotas(self, params = None, **kwargs):
        """Fetch all tenants' quotas."""
        return self._get(self.quotas_path, params = params, **kwargs)

    def show_quota(self, tenant_id, params = None, **kwargs):
        """Fetch information of a certain tenant's quotas.

        :param tenant_id: ID of the tenant.
        """
        return self._get(self.quota_path % (tenant_id), params=params, **kwargs)

    def update_quota(self, tenant_id, quota_body, **kwargs):
        """Update a tenant's quotas.

        :param tenant_id: ID of the tenant.
        :param kwargs: update values.
        """
        body = {
            "quota" : quota_body
        }
        return self._put(self.quota_path % (tenant_id), body = body, **kwargs)

    def delete_quota(self, tenant_id, **kwargs):
        """Delete the specified tenant's quota values.

        :param tenant_id: ID of the tenant.
        """
        return self._delete(self.quota_path % (tenant_id), **kwargs)
