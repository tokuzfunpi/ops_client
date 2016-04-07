from ops_client.manager.manila import ManilaBaseManager


class LimitsManager(ManilaBaseManager):
    """Manager object used to interact with limits resource."""

    def get(self, **kwargs):
        """Get a specific extension.

        :rtype: :class:`Limits`
        """
        return self._get("/limits", **kwargs)
