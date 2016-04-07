from ops_client.manager.heat import HeatBaseManager

class TemplateManager(HeatBaseManager):
    def get(self, stack_name, stack_id, **kwargs):
        """Get the template content for a specific stack as a parsed JSON
        object.

        :param stack_id: Stack ID to get the template for
        """
        url = '/stacks/%s/%s/template' %(stack_name, stack_id)
        return self._get(url, **kwargs)

    def validate(self, template_url=None, template=None, environment=None,
                 show_nested=False, extra_body={}, **kwargs):
        """Validate a stack template."""
        body = extra_body
        if template_url:
            body['template_url'] = template_url
        if template:
            body['template'] = template
        if environment:
            body['environment'] = environment
        url = '/validate'
        if show_nested:
            url += '?show_nested=True'
        return self._post(url, body, **kwargs)