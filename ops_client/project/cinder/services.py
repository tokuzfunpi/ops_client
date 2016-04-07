from ops_client.manager.cinder import CinderBaseManager

class ServiceManager(CinderBaseManager):

    def list(self, host=None, binary=None, **kwargs):
        """
        Describes service list for host.

        :param host: destination host name.
        :param binary: service binary.
        """
        url = "/os-services"
        filters = []
        if host:
            filters.append("host=%s" % host)
        if binary:
            filters.append("binary=%s" % binary)
        if filters:
            url = "%s?%s" % (url, "&".join(filters))
        return self._get(url, **kwargs)

    def enable(self, host, binary, **kwargs):
        """Enable the service specified by hostname and binary.

        :param host: destination host name.
        :param binary: service binary.
        """
        body = {"host": host, "binary": binary}
        return self._put("/os-services/enable", body, **kwargs)

    def disable(self, host, binary, **kwargs):
        """Disable the service specified by hostname and binary.

        :param host: destination host name.
        :param binary: service binary.
        """
        body = {"host": host, "binary": binary}
        return self._put("/os-services/disable", body, **kwargs)

    def disable_log_reason(self, host, binary, reason, **kwargs):
        """Disable the service with reason.

        :param host: destination host name.
        :param binary: service binary.
        :param reason: disable reason.
        """
        body = {"host": host, "binary": binary, "disabled_reason": reason}
        return self._put("/os-services/disable-log-reason", body, **kwargs)
