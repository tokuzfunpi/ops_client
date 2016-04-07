"""
Limit interface.
"""

from ops_client.manager.nova import NovaBaseManager

class LimitsManager(NovaBaseManager):

    def get(self, params = None, response_key = True, **kwargs):
        """
        Get a specific extension.

        :rtype: :class:`Limits`
        """
        if response_key :
            return self._get("/limits", "limits", params=params, **kwargs)
        else :
            return self._get("/limits", params=params, **kwargs)