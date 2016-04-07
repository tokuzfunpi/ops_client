"""
Server group interface.
"""

from ops_client.manager.nova import NovaBaseManager

class ServerGroupsManager(NovaBaseManager):

    def list(self, response_key = True, **kwargs):
        """Get a list of all server groups.

        :rtype: list of :class:`ServerGroup`.
        """
        if response_key :
            return self._get('/os-server-groups', 'server_groups', **kwargs)
        else :
            return self._get('/os-server-groups', **kwargs)

    def get(self, group_id, response_key = True, **kwargs):
        """Get a specific server group.

        :param id: The ID of the :class:`ServerGroup` to get.
        :rtype: :class:`ServerGroup`
        """
        if response_key :
            return self._get('/os-server-groups/%s' % group_id,
                             'server_group', **kwargs)
        else :
            return self._get('/os-server-groups/%s' % group_id, **kwargs)

    def delete(self, group_id, **kwargs):
        """Delete a specific server group.

        :param id: The ID of the :class:`ServerGroup` to delete.
        """
        return self._delete('/os-server-groups/%s' % group_id, **kwargs)

    def create(self, response_key = True, server_group_body = None, **kwargs):
        """Create (allocate) a server group.

        :rtype: list of :class:`ServerGroup`
        """
        if server_group_body and type(server_group_body) == dict :
            body = {'server_group': server_group_body}
        if response_key :
            return self._post('/os-server-groups', body,
                              'server_group', **kwargs)
        else :
            return self._post('/os-server-groups', body, **kwargs)
