"""
Fping interface. (Not supported now.)
"""

from ops_client.manager.nova import NovaBaseManager

class FpingManager(NovaBaseManager):

    def list(self, all_tenants=False, include=[], exclude=[],
             response_key = True, **kwargs):
        """
        Fping all servers.

        :rtype: list of :class:`Fping`.
        """
        params = []
        if all_tenants:
            params.append("all_tenants=1")
        if include:
            params.append("include=%s" % ",".join(include))
        elif exclude:
            params.append("exclude=%s" % ",".join(exclude))
        uri = "/os-fping"
        if params:
            uri = "%s?%s" % (uri, "&".join(params))
        if response_key :
            return self._get(uri, "servers", **kwargs)
        else :
            return self._get(uri, **kwargs)

    def get(self, server_id, response_key = True, **kwargs):
        """
        Fping a specific server.

        :param network: ID of the server to fping.
        :rtype: :class:`Fping`
        """
        if response_key :
            return self._get("/os-fping/%s" % server_id, "server", **kwargs)
        else :
            return self._get("/os-fping/%s" % server_id, **kwargs)