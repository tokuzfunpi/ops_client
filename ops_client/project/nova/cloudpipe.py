"""
Cloudpipe interface.
"""

from ops_client.manager.nova import NovaBaseManager

class CloudpipeManager(NovaBaseManager):

    def create(self, project_id, response_key = True, **kwargs):
        """
        Launch a cloudpipe instance.

        :param project: UUID of the project (tenant) for the cloudpipe
        """
        body = {'cloudpipe': {'project_id': project_id}}
        if response_key :
            return self._post('/os-cloudpipe', body, 'instance_id', **kwargs)
        else :
            return self._post('/os-cloudpipe', body, **kwargs)

    def list(self, response_key = True, **kwargs):
        """
        Get a list of cloudpipe instances.
        """
        if response_key :
            return self._get('/os-cloudpipe', 'cloudpipes', **kwargs)
        else :
            return self._get('/os-cloudpipe', **kwargs)

    def update(self, address, port, **kwargs):
        """
        Update VPN address and port for all networks associated
        with the project defined by authentication

        :param address: IP address
        :param port: Port number
        """
        body = {'configure_project': {'vpn_ip': address,
                                      'vpn_port': port}}
        return self._put("/os-cloudpipe/configure-project", body, **kwargs)
