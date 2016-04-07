from ops_client.manager.heat import HeatBaseManager

class SoftwareDeploymentManager(HeatBaseManager):
    def list(self, response_key=True, **kwargs):
        """Get a list of software deployments.
        :rtype: list of :class:`SoftwareDeployment`
        """
        url = '/software_deployments'
        if response_key:
            return self._get(url, 'software_deployments', **kwargs)
        else:
            return self._get(url, **kwargs)

    def metadata(self, server_id, response_key=True, **kwargs):
        """Get a grouped collection of software deployment metadata for a
        given server.
        :rtype: list of :class:`SoftwareDeployment`
        """
        url = '/software_deployments/metadata/%s' % server_id
        if response_key:
            return self._get(url, 'metadata', **kwargs)
        else:
            return self._get(url, **kwargs)

    def get(self, deployment_id, response_key=True, **kwargs):
        """Get the details for a specific software deployment.

        :param deployment_id: ID of the software deployment
        """
        url = '/software_deployments/%s' %deployment_id
        if response_key:
            return self._get(url, 'software_deployment', **kwargs)
        else:
            return self._get(url, **kwargs)

    def create(self, config_id, server_id, action,
               stack_user_project_id=None, status=None, status_reason=None,
               extra_body={}, response_key=True, **kwargs):
        """Create a software deployment."""
        body = extra_body
        body['config_id'] = config_id
        body['server_id'] = server_id
        body['action'] = action
        if stack_user_project_id:
            body['stack_user_project_id'] = stack_user_project_id
        if status:
            body['status'] = status
        if status_reason:
            body['status_reason'] = status_reason
        url = '/software_deployments'
        if response_key:
            return self._post(url, body, 'software_deployment', **kwargs)
        else:
            return self._post(url, body, **kwargs)

    def update(self, deployment_id, action=None, status=None,
               status_reason=None, output_values=None, extra_body={},
               response_key=True, **kwargs):
        """Update a software deployment."""
        body = extra_body
        if action:
            body['action'] = action
        if status:
            body['status'] = status
        if status_reason:
            body['status_reason'] = status_reason
        if output_values:
            body['output_values'] = output_values
        url = '/software_deployments/%s' %deployment_id
        if response_key:
            return self._put(url, body, 'software_deployment', **kwargs)
        else:
            return self._put(url, body, **kwargs)

    def delete(self, deployment_id, **kwargs):
        """Delete a software deployment."""
        url = '/software_deployments/%s' %deployment_id
        return self._delete(url, **kwargs)