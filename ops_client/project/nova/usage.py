"""
Usage interface.
"""

from ops_client.manager.nova import NovaBaseManager

class UsageManager(NovaBaseManager):

    def list(self, start, end, detailed=False, response_key = True, **kwargs):
        """
        Get usage for all tenants

        :param start: :class:`datetime.datetime` Start date
        :param end: :class:`datetime.datetime` End date
        :param detailed: Whether to include information about each
                         instance whose usage is part of the report
        :rtype: list of :class:`Usage`.
        """
        if response_key :
            return self._get(
                        "/os-simple-tenant-usage?start=%s&end=%s&detailed=%s" %
                            (start.isoformat(), end.isoformat(), 
                             int(bool(detailed))),
                        "tenant_usages", **kwargs)
        else :
            return self._get(
                        "/os-simple-tenant-usage?start=%s&end=%s&detailed=%s" %
                            (start.isoformat(), end.isoformat(), 
                             int(bool(detailed))),
                        **kwargs)

    def get(self, tenant_id, start, end, response_key = True, **kwargs):
        """
        Get usage for a specific tenant.

        :param tenant_id: Tenant ID to fetch usage for
        :param start: :class:`datetime.datetime` Start date
        :param end: :class:`datetime.datetime` End date
        :rtype: :class:`Usage`
        """
        if response_key :
            return self._get("/os-simple-tenant-usage/%s?start=%s&end=%s" %
                                 (tenant_id, start.isoformat(), 
                                  end.isoformat()),
                             "tenant_usage", **kwargs)
        else :
            return self._get("/os-simple-tenant-usage/%s?start=%s&end=%s" %
                                 (tenant_id, start.isoformat(), 
                                  end.isoformat()),
                             **kwargs)
