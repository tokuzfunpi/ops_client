from ops_client.manager.keystone import KeystoneBaseManager

class RoleManager(KeystoneBaseManager):
    """Represents an Identity role.

    Attributes:
        * id: a uuid that identifies the role
        * name: user-facing identifier

    """
    collection_key = 'roles'
    key = 'role'

    def _role_grants_base_url(self, user_id, group_id, domain_id, project_id):
        params = {}

        if project_id:
            params['project_id'] = project_id
            base_url = '/projects/%(project_id)s'
        elif domain_id:
            params['domain_id'] = domain_id
            base_url = '/domains/%(domain_id)s'

        if user_id:
            params['user_id'] = user_id
            base_url += '/users/%(user_id)s'
        elif group_id:
            params['group_id'] = group_id
            base_url += '/groups/%(group_id)s'

        return base_url % params

    def _require_domain_xor_project(self, domain_id, project_id):
        if (domain_id and project_id) or (not domain_id and not project_id):
            msg = 'Specify either a domain or project, not both'
            raise Exception(msg)

    def _require_user_xor_group(self, user_id, group_id):
        if (user_id and group_id) or (not user_id and not group_id):
            msg = 'Specify either a user or group, not both'
            raise Exception(msg)

    def create_role(self, name):
        return self.create(name=name)

    def get_role(self, role_id):
        return self.get(role_id = role_id)

    def list_role(self, user_id = None, group_id = None, domain_id = None, 
                  project_id = None, **kwargs):
        """Lists roles and role grants.

        If no arguments are provided, all roles in the system will be
        listed.

        If a user or group is specified, you must also specify either a
        domain or project to list role grants on that pair. And if
        ``**kwargs`` are provided, then also filter roles with
        attributes matching ``**kwargs``.
        """
        if user_id or group_id:
            self._require_user_xor_group(user_id, group_id)
            self._require_domain_xor_project(domain_id, project_id)

            return self.list(
                base_url=self._role_grants_base_url(user_id, group_id,
                                                    domain_id, project_id),
                **kwargs)
        return self.list()

    def update_role(self, role_id, name = None):
        return self.update(role_id = role_id, name = name)

    def delete_role(self, role_id):
        return self.delete(role_id = role_id)

    def grant_role(self, role_id, user_id = None, group_id = None, 
                   domain_id = None, project_id = None):
        self._require_domain_xor_project(domain_id, project_id)
        self._require_user_xor_group(user_id, group_id)

        return self.put(
            base_url = self._role_grants_base_url(user_id, group_id, 
                                                domain_id, project_id),
            role_id = role_id)

    def check_role(self, role_id, user_id = None, group_id = None, 
                   domain_id = None, project_id = None):
        self._require_domain_xor_project(domain_id, project_id)
        self._require_user_xor_group(user_id, group_id)

        return self.head(
            base_url = self._role_grants_base_url(user_id, group_id, 
                                                domain_id, project_id),
            role_id = role_id)

    def revoke(self, role_id, user_id = None, group_id = None, 
              domain_id = None, project_id = None):
        self._require_domain_xor_project(domain_id, project_id)
        self._require_user_xor_group(user_id, group_id)

        return self.delete(
            base_url = self._role_grants_base_url(user_id, group_id, 
                                                domain_id, project_id),
            role_id = role_id)
