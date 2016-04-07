"""
Agent interface
"""

from ops_client.manager.nova import NovaBaseManager

class AgentManager(NovaBaseManager):

    def list(self, hypervisor=None, response_key = True, **kwargs):
        """List all agent builds.

        :param hypervisor: (optional) (string)
        """
        url = "/os-agents"
        if hypervisor:
            url = "/os-agents?hypervisor=%s" % hypervisor
        if response_key :
            return self._get(url, "agents", **kwargs)
        else :
            return self._get(url, **kwargs)

    def update(self, agent_id, version, url, md5hash,
               response_key = True, **kwargs):
        """Update an existing agent build.

        :param agent_id: Agent's ID. (uuid)
        :param version: (string)
        :param url: (string)
        :param md5hash: (string)
        """
        body = {'para': {
                       'version': version,
                       'url': url,
                       'md5hash': md5hash}}
        if response_key :
            return self._put('/os-agents/%s' % agent_id, body, 'agent', **kwargs)
        else :
            return self._put('/os-agents/%s' % agent_id, body, **kwargs)

    def create(self, os, architecture, version, url,
               md5hash, hypervisor, response_key = True, **kwargs):
        """Create a new agent build.

        :param os: (string)
        :param architecture: (string)
        :param version: (string)
        :param url: (string)
        :param md5hash: (string)
        :param hypervisor: (string)
        """
        body = {'agent': {
                        'hypervisor': hypervisor,
                        'os': os,
                        'architecture': architecture,
                        'version': version,
                        'url': url,
                        'md5hash': md5hash}}
        if response_key :
            return self._post('/os-agents', body, 'agent', **kwargs)
        else :
            return self._post('/os-agents', body, **kwargs)

    def delete(self, agent_id, **kwargs):
    	"""Deletes an existing agent build.

        :param agent_id: Agent's ID. (uuid)
        """
        return self._delete('/os-agents/%s' % agent_id, **kwargs)
