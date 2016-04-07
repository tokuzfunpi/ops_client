from ops_client.manager.heat import HeatBaseManager

class ServiceManager(HeatBaseManager):
    def list(self, response_key=True, **kwargs):
        """Get a list of services.
        :rtype: list of :class:`Service`
        """
        url = '/services'
        if response_key:
            return self._get(url, "services", **kwargs)
        else:
            return self._get(url, **kwargs)
