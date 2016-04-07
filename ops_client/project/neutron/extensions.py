from ops_client.manager.neutron import NeutronBaseManager

class ExtensionManager(NeutronBaseManager):

    def list_extensions(self, params = None, **kwargs):
        """List all extensions."""
        return self._get(self.extensions_path, params = params, **kwargs)

    def show_extension(self, ext_alias, params = None, **kwargs):
        """Show information of a given resource.

        :param ext_alias: (string)
        """
        return self._get(self.extension_path % ext_alias, 
                         params = params, **kwargs)
