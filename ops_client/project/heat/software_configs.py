from ops_client.manager.heat import HeatBaseManager

class SoftwareConfigManager(HeatBaseManager):
    def get(self, config_id, response_key=True, **kwargs):
        """Get the details for a specific software config.

        :param config_id: ID of the software config
        """
        url = '/software_configs/%s' % config_id
        if response_key:
            return self._get(url, 'software_config', **kwargs)
        else:
            return self._get(url, **kwargs)

    def create(self, extra_body={}, config=None, group=None, name=None,
               inputs=None, outputs=None, options=None, 
               response_key=True, **kwargs):
        """Create a software config."""
        body = extra_body
        url = '/software_configs'
        if config:
            body['config'] = config
        if group:
            body['group'] = group
        if name:
            body['name'] = name
        if inputs:
            body['inputs'] = inputs
        if outputs:
            body['outputs'] = outputs
        if options:
            body[options] = options
        if response_key:
            return self._post(url, body, 'software_config', **kwargs)
        else:
            return self._post(url, body, **kwargs)

    def delete(self, config_id, **kwargs):
        """Delete a software config."""
        url = '/software_configs/%s' % config_id
        return self._delete(url, **kwargs)

    def list(self, response_key=True, **kwargs):
        url = '/software_configs'
        if response_key:
            return self._get(url, 'software_configs', **kwargs)
        else:
            return self._get(url, **kwargs)