from ops_client.manager.trove import TroveBaseManager

class SecurityGroupManager(TroveBaseManager):

    def list(self, limit = None, marker = None, response_key = True, **kwargs):
        """Get a list of all security groups.

        :rtype: list of :class:`SecurityGroup`.
        """
        url = self.build_url("/security-groups",
                             limit = limit,
                             marker = marker)
        if response_key :
            return self._get(url, "security_groups", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, security_group, response_key = True, **kwargs):
        """Get a specific security group.

        :rtype: :class:`SecurityGroup`
        """
        if response_key :
            return self._get("/security-groups/%s" % security_group,
                             "security_group", **kwargs)
        else :
            return self._get("/security-groups/%s" % security_group, **kwargs)