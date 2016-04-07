from ops_client.manager.trove import TroveBaseManager

class LimitManager(TroveBaseManager):

    def list(self, response_key = True, **kwargs):
        """Retrieve the limits."""
        if response_key :
            return self._get("/limits", "limits", **kwargs)
        else :
            return self._get("/limits", **kwargs)