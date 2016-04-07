from ops_client.manager.keystone import KeystoneBaseManager

class UserManager(KeystoneBaseManager):
    """Represents an Identity user.

    Attributes:
        * id: a uuid that identifies the user

    """
    collection_key = 'users'
    key = 'user'

    def _require_user_and_group(self, user_id, group_id):
        if not (user_id and group_id):
            msg = 'Specify both a user and a group'
            raise Exception(msg)

    def create_user(self, name, domain_id = None, project_id = None, 
                    password = None, email = None, description = None, 
                    enabled = True):
        """Create a user.

        .. warning::

          The project argument is deprecated, use default_project instead.

        If both default_project and project is provided, the default_project
        will be used.
        """
        return self.create(
            name=name,
            domain_id = domain_id,
            project_id = project_id,
            password = password,
            email = email,
            description = description,
            enabled = enabled)

    def list_user(self, project_id = None, domain_id = None, group_id = None, 
                  **kwargs):
        """List users.

        If project, domain or group are provided, then filter
        users with those attributes.

        If ``**kwargs`` are provided, then filter users with
        attributes matching ``**kwargs``.

        .. warning::

          The project argument is deprecated, use default_project instead.

        If both default_project and project is provided, the default_project
        will be used.
        """
        if group_id:
            base_url = '/groups/%s' % group_id
        else:
            base_url = None

        return self.list(
            base_url=base_url,
            domain_id = domain_id,
            project_id = project_id,
            **kwargs)

    def get_user(self, user_id):
        return self.get(user_id = user_id)

    def update_user(self, user_id, name = None, domain_id = None, 
                    project_id = None, password = None, email = None, 
                    description = None, enabled = None):
        """Update a user.

        .. warning::

          The project argument is deprecated, use default_project instead.

        If both default_project and project is provided, the default_project
        will be used.
        """
        return self.update(
            user_id = user_id,
            name = name,
            domain_id = domain_id,
            project_id = project_id,
            password = password,
            email = email,
            description = description,
            enabled = enabled)

    def add_to_group(self, user_id, group_id):
        self._require_user_and_group(user_id, group_id)

        base_url = '/groups/%s' % group_id
        return self.put(
            base_url = base_url,
            user_id = user_id)

    def check_in_group(self, user_id, group_id):
        self._require_user_and_group(user_id, group_id)

        base_url = '/groups/%s' % group_id
        return self.head(
            base_url = base_url,
            user_id = user_id)

    def remove_from_group(self, user_id, group_id):
        self._require_user_and_group(user_id, group_id)

        base_url = '/groups/%s' % group_id
        return self.delete(
            base_url = base_url,
            user_id = user_id)

    def delete_user(self, user_id):
        return self.delete(user_id = user_id)
