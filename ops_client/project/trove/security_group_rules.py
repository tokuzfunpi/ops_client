from ops_client.manager.trove import TroveBaseManager

class SecurityGroupRuleManager(TroveBaseManager):

    def create(self, group_id, cidr, response_key = True, **kwargs):
        """Create a new security group rule."""
        body = {"security_group_rule": {
            "group_id": group_id,
            "cidr": cidr
        }}
        if response_key :
            return self._post("/security-group-rules", body,
                              "security_group_rule", **kwargs)
        else :
            return self._post("/security-group-rules", body, **kwargs)

    def delete(self, security_group_rule, **kwargs):
        """Delete the specified security group rule.

        :param security_group_rule: The security group rule to delete
        """
        return self._delete("/security-group-rules/%s" % security_group_rule,
                            **kwargs)

    def list(self, group_id, response_key = True, **kwargs):
        if response_key :
            return self._get("/security-groups/%s" % group_id,
                             "security_group", **kwargs)
        else :
            return self._get("/security-groups/%s" % group_id, **kwargs)