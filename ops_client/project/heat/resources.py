import six
from six.moves.urllib import parse
from ops_client.manager.heat import HeatBaseManager

class ResourceManager(HeatBaseManager):
    def list(self, stack_name, stack_id, filters=None, response_key=True, 
             **kwargs):
        """Get a list of resources.
        :rtype: list of :class:`Resource`
        """
        params = {}
        if filters:
            params.update(filters)
        url = '/stacks/%s/%s/resources' % (stack_name, stack_id)
        if params:
            url += '?%s' % parse.urlencode(params, True)
        if response_key:
            return self._get(url, "resources", **kwargs)
        else:
            return self._get(url, **kwargs)

    def get(self, stack_name, stack_id, resource_name,
            with_attr=None, response_key=True, **kwargs):
        """Get the details for a specific resource.

        :param stack_id: ID of stack containing the resource
        :param resource_name: ID of resource to get the details for
        :param with_attr: Attributes to show
        """
        url = '/stacks/%s/%s/resources/%s' \
                 % (stack_name, stack_id, resource_name)
        if with_attr:
            params = {'with_attr': with_attr}
            url += '?%s' % parse.urlencode(params, True)

        if response_key:
            return self._get(url, "resource", **kwargs)
        else:
            return self._get(url, **kwargs)

    def metadata(self, stack_name, stack_id, resource_name,
                 response_key=True, **kwargs):
        """Get the metadata for a specific resource.

        :param stack_id: ID of stack containing the resource
        :param resource_name: ID of resource to get metadata for
        """
        url = '/stacks/%s/%s/resources/%s/metadata' \
                 % (stack_name, stack_id, resource_name)
        if response_key:
            return self._get(url, "metadata", **kwargs)
        else:
            return self._get(url, **kwargs)

    def signal(self, stack_name, stack_id, resource_name, data=None, **kwargs):
        """Signal a specific resource.

        :param stack_id: ID of stack containing the resource
        :param resource_name: ID of resource to send signal to
        """
        url = '/stacks/%s/%s/resources/%s/signal' \
                 % (stack_name, stack_id, resource_name)
        return self.base_post(url, **kwargs)