from ops_client.manager.keystone import KeystoneBaseManager

class GroupManager(KeystoneBaseManager):
    """Represents an Identity user group.

    Attributes:
        * id: a uuid that identifies the group
        * name: group name
        * description: group description

    """
    collection_key = 'groups'
    key = 'group'

    def create_group(self, name, domain_id = None, description = None):
        return self.create(
            name=name,
            domain_id = domain_id,
            description = description)

    def list_group(self, user_id = None, domain_id = None, **kwargs):
        """List groups.

        If domain or user is provided, then filter groups with
        that attribute.

        If ``**kwargs`` are provided, then filter groups with
        attributes matching ``**kwargs``.
        """
        if user_id:
            base_url = '/users/%s' % user_id
        else:
            base_url = None
        return self.list(
            base_url=base_url,
            domain_id = domain_id,
            **kwargs)

    def get_group(self, group_id):
        return self.get(group_id = group_id)

    def update_group(self, group_id, name = None, description = None):
        return self.update(
            group_id = group_id,
            name = name,
            description = description)

    def delete_group(self, group_id):
        return self.delete(group_id = group_id)
