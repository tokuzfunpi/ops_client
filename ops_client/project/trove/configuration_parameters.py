from ops_client.manager.trove import TroveBaseManager

class ConfigurationParameterManager(TroveBaseManager):

    def parameters(self, datastore, version, response_key = True, **kwargs):
        """Get a list of valid parameters that can be changed."""
        if response_key :
            return self._get("/datastores/%s/versions/%s/parameters" %
                             (datastore, version), "configuration-parameters",
                             **kwargs)
        else :
            return self._get("/datastores/%s/versions/%s/parameters" %
                             (datastore, version), **kwargs)

    def get_parameter(self, datastore, version, key, **kwargs):
        """Get a list of valid parameters that can be changed."""
        return self._get("/datastores/%s/versions/%s/parameters/%s" %
                         (datastore, version, key), **kwargs)

    def parameters_by_version(self, version, response_key = True, **kwargs):
        """Get a list of valid parameters that can be changed."""
        if response_key :
            return self._get("/datastores/versions/%s/parameters" % version,
                             "configuration-parameters", **kwargs)
        else :
            return self._get("/datastores/versions/%s/parameters" % version,
                             **kwargs)

    def get_parameter_by_version(self, version, key, **kwargs):
        """Get a list of valid parameters that can be changed."""
        return self._get("/datastores/versions/%s/parameters/%s" %
                         (version, key), **kwargs)
