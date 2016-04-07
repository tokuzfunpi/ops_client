from six.moves.urllib import parse
from ops_client.manager.heat import HeatBaseManager

class ResourceTypeManager(HeatBaseManager):
    def list(self, filters=None, response_key=True, **kwargs):
        """Get a list of resource types.
        :rtype: list of :class:`ResourceType`
        """

        url = '/resource_types'
        params = {}
        if filters:
            params.update(filters)
            url += '?%s' % parse.urlencode(params, True)

        if response_key:
            return self._get(url, 'resource_types', **kwargs)
        else:
            return self._get(url, **kwargs)

    def get(self, resource_type, **kwargs):
        """Get the details for a specific resource_type.

        :param resource_type: name of the resource type to get the details for
        """
        url = '/resource_types/%s' % resource_type

        return self._get(url, **kwargs)

    def get_template(self, resource_type, template_type=None, **kwargs):
        url = '/resource_types/%s/template' % resource_type
        if template_type:
            url += '?%s' % parse.urlencode(
                {'template_type': template_type}, True)
        
        return self._get(url, **kwargs)