from ops_client.manager.cinder import CinderBaseManager

class LimitsManager(CinderBaseManager):

    def get(self, **kwargs):
        """Get a specific extension.

        :rtype: :class:`Limits`
        """
        return self._get("/limits", **kwargs)
