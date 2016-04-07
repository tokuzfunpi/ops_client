import six
from six.moves.urllib import parse
from ops_client.manager.heat import HeatBaseManager

class StackManager(HeatBaseManager):
    def list(self, filters=None, response_key=True, **kwargs):
        """Get a list of stacks.

        :param limit: maximum number of stacks to return
        :param marker: begin returning stacks that appear later in the stack
                       list than that represented by this stack id
        :param filters: dict of direct comparison filters that mimics the
                        structure of a stack object
        :rtype: list of :class:`Stack`
        """

        params = {}
        if filters:
            params.update(filters)
        url = '/stacks?%s' % parse.urlencode(params, True)
        if response_key:
            return self._get(url, 'stacks', **kwargs)
        else:
            return self._get(url, **kwargs)

    def _gen_body(self, extra_body, template_url=None, disable_rollback=True,
                  template=None, files=None, parameters={}, tags='', 
                  timeout_mins=None, adopt_stack_data=None, environment=None):
        body = extra_body
        if template_url:
            body['template_url'] = template_url
        if template:
            body['template'] = template
        if files:
            body['files'] = files
        if parameters:
            body['parameters'] = parameters
        if disable_rollback:
            body['disable_rollback'] = disable_rollback
        if tags:
            body['tags'] = tags
        if timeout_mins:
            body['timeout_mins'] = timeout_mins
        if environment:
            body['environment'] = environment
        if adopt_stack_data is not None:
            if type(adopt_stack_data) is dict:
                body['adopt_stack_data'] = adopt_stack_data
            else:
                raise TypeError('adopt_stack_data type should be dict.')
        return body

    def preview(self, stack_name, template_url=None, disable_rollback=True,
                template=None, files=None, parameters={}, extra_body={},
                response_key=True, **kwargs):
        """Preview a stack."""
        body = self._gen_body(extra_body,
                              template_url=template_url,
                              disable_rollback=disable_rollback,
                              template=template,
                              files=files,
                              parameters=parameters)
        body['stack_name'] = stack_name
        url = '/stacks/preview'
        if response_key:
            return self._post(url, body, 'stack', **kwargs)
        else:
            return self._post(url, body, **kwargs)

    def create(self, stack_name, template_url=None, disable_rollback=True,
               template=None, files=None, parameters={}, extra_body={},
               response_key=True, tags='', timeout_mins=None,
               adopt_stack_data=None, **kwargs):
        """Create a stack."""
        body = self._gen_body(extra_body,
                              template_url=template_url,
                              disable_rollback=disable_rollback,
                              template=template,
                              files=files,
                              parameters=parameters,
                              tags=tags,
                              timeout_mins=timeout_mins,
                              adopt_stack_data=adopt_stack_data)
        body['stack_name'] = stack_name
        url = '/stacks'
        if response_key:
            return self._post(url, body, 'stack', **kwargs)
        else:
            return self._post(url, body, **kwargs)

    def update(self, stack_name, stack_id, extra_body={},
               template_url=None, template=None, environment=None, files=None, 
               tags=None, parameters=None, timeout_mins=None, **kwargs):
        """Update a stack."""
        body = self._gen_body(extra_body,
                              template_url=template_url,
                              template=template,
                              environment=environment,
                              files=files,
                              tags=tags,
                              parameters=parameters,
                              timeout_mins=timeout_mins)
        url = '/stacks/%s/%s' %(stack_name, stack_id)
        return self._put(url, body, **kwargs)

    def preview_update(self, stack_name, stack_id, extra_body={},
                       template_url=None, template=None, environment=None,
                       files=None, tags=None, parameters=None,
                       timeout_mins=None, **kwargs):
        """Preview a stack update."""
        body = self._gen_body(extra_body,
                              template_url=template_url,
                              template=template,
                              environment=environment,
                              files=files,
                              tags=tags,
                              parameters=parameters,
                              timeout_mins=timeout_mins)
        url = '/stacks/%s/%s/preview' %(stack_name, stack_id)
        return self._put(url, body, **kwargs)

    def delete(self, stack_name, stack_id, **kwargs):
        """Delete a stack."""
        url = '/stacks/%s/%s' %(stack_name, stack_id)
        return self._delete(url, **kwargs)

    def abandon(self, stack_name, stack_id, **kwargs):
        """Abandon a stack."""
        url = '/stacks/%s/%s/abandon' %(stack_name, stack_id)
        return self._delete(url, **kwargs)

    def get(self, stack_name, stack_id, response_key=True, **kwargs):
        """Get the metadata for a specific stack.

        :param stack_id: Stack ID to lookup
        """
        url = '/stacks/%s/%s' %(stack_name, stack_id)
        if response_key:
            return self._get(url, 'stack', **kwargs)
        else:
            return self._get(url, **kwargs)