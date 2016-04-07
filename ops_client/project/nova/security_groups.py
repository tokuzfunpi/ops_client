"""
Security group interface.
"""
from ops_client.manager.nova import NovaBaseManager

class SecurityGroupManager(NovaBaseManager):

    def create(self, name, description, response_key = True, **kwargs):
        """
        Create a security group

        :param name: name for the security group to create
        :param description: description of the security group
        :rtype: the security group object
        """
        body = {"security_group": {"name": name, 'description': description}}
        if response_key :
            return self._post('/os-security-groups', body,
                              'security_group', **kwargs)
        else :
            return self._post('/os-security-groups', body, **kwargs)

    def update(self, group_id, name, description, response_key = True, **kwargs):
        """
        Update a security group

        :param group: The security group to update (group or ID)
        :param name: name for the security group to update
        :param description: description for the security group to update
        :rtype: the security group object
        """
        body = {"security_group": {"name": name, 'description': description}}
        if response_key :
            return self._put('/os-security-groups/%s' % group_id,
                                body, 'security_group', **kwargs)
        else :
            return self._put('/os-security-groups/%s' % group_id,
                                body, **kwargs)

    def delete(self, group_id):
        """
        Delete a security group

        :param group: The security group to delete (group or ID)
        :rtype: None
        """
        return self._delete('/os-security-groups/%s' % group_id)

    def get(self, group_id, response_key = True, **kwargs):
        """
        Get a security group

        :param group_id: The security group to get by ID
        :rtype: :class:`SecurityGroup`
        """
        if response_key :
            return self._get('/os-security-groups/%s' % group_id,
                             'security_group', **kwargs)
        else: 
            return self._get('/os-security-groups/%s' % group_id, **kwargs)

    def list(self, params = None, response_key = True, **kwargs):
        """
        Get a list of all security_groups

        :rtype: list of :class:`SecurityGroup`
        """
        if response_key :
            return self._get('/os-security-groups',
                              'security_groups', params=params, **kwargs)
        else :
            return self._get('/os-security-groups',
                              params=params, **kwargs)
