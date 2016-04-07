from ops_client.manager.heat import HeatBaseManager

class BuildInfoManager(HeatBaseManager):
    def get(self, **kwargs):
        """Get build infos.
        :rtype: list of :class:`BuildInfo`
        """
        url = '/build_info'
        return self._get(url, **kwargs)
