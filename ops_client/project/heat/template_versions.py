from ops_client.manager.heat import HeatBaseManager

class TemplateVersionManager(HeatBaseManager):
    def list(self, response_key=True, **kwargs):
        """Get a list of template versions.
        :rtype: list of :class:`TemplateVersion`
        """
        url = '/template_versions'
        if response_key:
            return self._get(url, 'template_versions', **kwargs)
        else:
            return self._get(url, **kwargs)

    def get(self, template_version, response_key=True, **kwargs):
        """Get a list of functions for a specific resource_type.

        :param template_version: template version to get the functions for
        """
        url = '/template_versions/%s/functions' % (template_version)
        if response_key:
            return self._get(url, 'template_functions', **kwargs)
        else:
            return self._get(url, **kwargs)