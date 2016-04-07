"""
Flavor access interface.
"""

from ops_client.manager.nova import NovaBaseManager

class FlavorAccessManager(NovaBaseManager):

    def _action(self, action, flavor_id, info = None, raw_body = None,
                response_key = True, **kwargs):
        """Perform a flavor action."""
        if not raw_body :
            body = {action: info}
        else :
            body = raw_body
        url = '/flavors/%s/action' % flavor_id
        return self._post(url, body, **kwargs)

    def list(self, flavor_id, response_key = True, **kwargs):
        """Get a list of all flavor Access.

        :param kwargs: falvor=flavor_id, or tenant=tenant_id

        .. warning::

           Filtered by tenant is not supported now.
        """
        if response_key :
            return self._get('/flavors/%s/os-flavor-access' % flavor_id,
                             'flavor_access', **kwargs)
        else :
            return self._get('/flavors/%s/os-flavor-access' % flavor_id,
                             **kwargs)

    def add_tenant_access(self, flavor_id, tenant_id, 
                          response_key = True, **kwargs):
        """Add a tenant to the given flavor access list.

        :param flavor_id: Flavor ID. (uuid)
        :param tenant_id: Tenant ID. (uuid)
        """
        info = {'tenant': tenant_id}
        return self._action('addTenantAccess', flavor_id,
                            info = info, response_key = response_key, **kwargs)

    def remove_tenant_access(self, flavor_id, tenant_id,
                             response_key = True, **kwargs):
        """Remove a tenant from the given flavor access list.

        :param flavor_id: Flavor ID. (uuid)
        :param tenant_id: Tenant ID. (uuid)
        """
        info = {'tenant': tenant_id}
        return self._action('removeTenantAccess', flavor_id,
                            info = info, response_key = response_key, **kwargs)
