"""
Floating IPs interface.
"""

from ops_client.manager.nova import NovaBaseManager

class FloatingIPManager(NovaBaseManager):

    def list(self, all_tenants=False, response_key = True, **kwargs):
        """
        List floating ips
        """
        url = '/os-floating-ips'
        if all_tenants:
            url += '?all_tenants=1'
        if response_key :
            return self._get(url, "floating_ips", **kwargs)
        else :
            return self._get(url, **kwargs)

    def create(self, pool = None, response_key = True, **kwargs):
        """
        Create (allocate) a  floating ip for a tenant
        """
        if response_key :
            return self._post("/os-floating-ips", {'pool': pool},
                              "floating_ip", **kwargs)
        else :
            return self._post("/os-floating-ips", {'pool': pool}, **kwargs)

    def delete(self, floating_ip_id, **kwargs):
        """
        Delete (deallocate) a  floating ip for a tenant

        :param floating_ip: The floating ip address to delete.
        """
        return self._delete("/os-floating-ips/%s" % floating_ip_id, **kwargs)

    def get(self, floating_ip_id, response_key = True, **kwargs):
        """
        Retrieve a floating ip
        """
        if response_key :
            return self._get("/os-floating-ips/%s" % floating_ip_id,
                             "floating_ip", **kwargs)
        else :
            return self._get("/os-floating-ips/%s" % floating_ip_id, **kwargs)
