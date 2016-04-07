from ops_client.manager.trove import TroveBaseManager

class ConfigurationManager(TroveBaseManager):

    def get(self, configuration, response_key = True, **kwargs):
        """Get a specific configuration.

        :rtype: :class:`Configurations`
        """
        if response_key :
            return self._get("/configurations/%s" % configuration,
                             "configuration", **kwargs)
        else :
            return self._get("/configurations/%s" % configuration, **kwargs)

    def instances(self, configuration, limit = None, marker = None,
                  response_key = True, **kwargs):
        """Get a list of instances on a configuration.

        :rtype: :class:`Configurations`
        """
        url = self.build_url("/configurations/%s/instances" % configuration,
                             limit = limit,
                             marker = marker)
        if response_key :
            return self._get(url, "instances", **kwargs)
        else :
            return self._get(url, **kwargs)
        
    def list(self, limit = None, marker = None, response_key = True, **kwargs):
        """Get a list of all configurations.

        :rtype: list of :class:`Configurations`.
        """
        url = self.build_url("/configurations", limit = limit, marker = marker)
        if response_key :
            return self._get(url, "configurations", **kwargs)
        else :
            return self._get(url, **kwargs)

    def create(self, name, values, description = None, datastore = None,
               datastore_version = None, response_key = True, **kwargs):
        """Create a new configuration."""
        body = {
            "configuration": {
                "name": name,
                "values": values
            }
        }
        datastore_obj = {}
        if datastore:
            datastore_obj["type"] = datastore
        if datastore_version:
            datastore_obj["version"] = datastore_version
        if datastore_obj:
            body["configuration"]["datastore"] = datastore_obj
        if description:
            body['configuration']['description'] = description
        if response_key :
            return self._post("/configurations", body,
                              "configuration", **kwargs)
        else :
            return self._post("/configurations", body, **kwargs)

    def update(self, configuration_id, values,
               name = None, description = None, **kwargs):
        """Update an existing configuration."""
        body = {
            "configuration": {
                "values": values
            }
        }
        if name:
            body['configuration']['name'] = name
        if description:
            body['configuration']['description'] = description

        return self._put("/configurations/%s" % configuration_id,
                         body, **kwargs)

    def edit(self, configuration_id, values, **kwargs):
        """Update an existing configuration."""
        body = {
            "configuration": {
                "values": values
            }
        }
        return self._patch("/configurations/%s" % configuration_id,
                           body, **kwargs)

    def delete(self, configuration_id, **kwargs):
        """Delete the specified configuration.

        :param configuration_id: The configuration id to delete
        """
        return self._delete("/configurations/%s" % configuration_id, **kwargs)