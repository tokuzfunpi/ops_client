from ops_client.manager.neutron import NeutronBaseManager

class SecurityGroupManager(NeutronBaseManager):

    def create_security_group(self, security_group_body, **kwargs):
        """Creates a new security group.

        :param security_group_body: security group values.
        """
        body = {
            "security_group" : security_group_body
        }
        return self._post(self.security_groups_path, body=body, **kwargs)

    def update_security_group(self, security_group_id, security_group_body,
                              **kwargs):
        """Updates a security group.

        :param security_group_id: ID of the security group.
        :param security_group_body: Body of the security group.
        """
        body = {
            "security_group" : security_group_body
        }
        return self._put(self.security_group_path %
                        security_group_id, body=body, **kwargs)

    def list_security_groups(self, params = None, **kwargs):
        """Fetches a list of all security groups for a tenant."""
        return self._get(self.security_groups_path, params = params, **kwargs)

    def show_security_group(self, security_group_id, params = None, **kwargs):
        """Fetches information of a certain security group.

        :param security_group_id: ID of the security group.
        """
        return self._get(self.security_group_path % (security_group_id),
                        params = params, **kwargs)

    def delete_security_group(self, security_group_id, **kwargs):
        """Deletes the specified security group.

        :param security_group: ID of the security group.
        """
        return self._delete(self.security_group_path % (security_group_id), 
                            **kwargs)

    def create_security_group_rule(self, security_group_id, direction = None, 
                                   rule_body = None, **kwargs):
        """Creates a new security group rule.

        :param security_group: ID of the security group.
        :param direction: 'engress' or 'ingress'
        """
        _body = {
            "security_group_id" : security_group_id,
            "direction":direction
        }
        if rule_body and type(rule_body) == dict :
            _body.update(rule_body)
        body = {"security_group_rule" : _body}
        return self._post(self.security_group_rules_path, body=body, **kwargs)

    def delete_security_group_rule(self, security_group_rule_id, **kwargs):
        """Deletes the specified security group rule.

        :param security_group_rule: ID of the security group rule.
        """
        return self._delete(self.security_group_rule_path %
                           (security_group_rule_id), **kwargs)

    def list_security_group_rules(self, params = None, **kwargs):
        """Fetches a list of all security group rules for a tenant."""
        return self._get(self.security_group_rules_path, params = params, 
                         **kwargs)

    def show_security_group_rule(self, security_group_rule_id, params = None, 
                                 **kwargs):
        """Fetches information of a certain security group rule.

        :param security_group_rule: ID of the security group rule.
        """
        return self._get(self.security_group_rule_path % \
                            (security_group_rule_id), params = params, **kwargs)
