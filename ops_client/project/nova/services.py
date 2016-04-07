"""
service interface
"""

from ops_client.manager.nova import NovaBaseManager

class ServiceManager(NovaBaseManager):

    def list(self, host=None, binary=None, response_key = True, **kwargs):
        """
        Describes cpu/memory/hdd info for host.

        :param host: destination host name.
        """
        url = "/os-services"
        filters = []
        if host:
            filters.append("host=%s" % host)
        if binary:
            filters.append("binary=%s" % binary)
        if filters:
            url = "%s?%s" % (url, "&".join(filters))
        if response_key :
            return self._get(url, "services", **kwargs)
        else :
            return self._get(url, **kwargs)

    def _update_body(self, host, binary, disabled_reason=None):
        body = {"host": host,
                "binary": binary}
        if disabled_reason is not None:
            body["disabled_reason"] = disabled_reason
        return body

    def enable(self, host, binary, response_key = True, **kwargs):
        """Enable the service specified by hostname and binary."""
        body = self._update_body(host, binary)
        if response_key :
            return self._put("/os-services/enable", body, "service", **kwargs)
        else :
            return self._put("/os-services/enable", body, **kwargs)

    def disable(self, host, binary, response_key = True, **kwargs):
        """Disable the service specified by hostname and binary."""
        body = self._update_body(host, binary)
        if response_key :
            return self._put("/os-services/disable", body, "service", **kwargs)
        else :
            return self._put("/os-services/disable", body, **kwargs)

    def disable_log_reason(self, host, binary, reason,
                           response_key = True, **kwargs):
        """Disable the service with reason."""
        body = self._update_body(host, binary, reason)
        if response_key :
            return self._put("/os-services/disable-log-reason",
                             body, "service", **kwargs)
        else :
            return self._put("/os-services/disable-log-reason", body, **kwargs)

    def delete(self, service_id, **kwargs):
        """Delete a service."""
        return self._delete("/os-services/%s" % service_id, **kwargs)
