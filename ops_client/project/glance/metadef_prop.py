from ops_client.manager.glance import GlanceBaseManager

class MetaDefPropertyManager(GlanceBaseManager):

    def create(self, namespace, name, title, p_type, extra_body = {}, **kwargs):
        """Create a property.

        :param namespace: Name of a namespace the property will belong.
        :param kwargs: Unpacked property object.
        """
        body = extra_body
        body['name'] = name
        body['title'] = title
        body['type'] = p_type
        url = '/metadefs/namespaces/%s/properties' %(namespace)
        return self._post(url, body, **kwargs)

    def update(self, namespace, prop_name, new_name, new_title, new_ptype,
               extra_body = {}, **kwargs):
        """Update a property.

        :param namespace: Name of a namespace the property belongs.
        :param prop_name: Name of a property (old one).
        :param kwargs: Unpacked property object.
        """
        url = '/metadefs/namespaces/%s/properties/%s' %(namespace, prop_name)
        body = extra_body
        body['name'] = new_name
        body['title'] = new_title
        body['type'] = new_ptype
        return self._put(url, body = body, **kwargs)

    def get(self, namespace, prop_name, **kwargs):
        url = '/metadefs/namespaces/%s/properties/%s' %(namespace, prop_name)
        return self._get(url, **kwargs)

    def list(self, namespace, **kwargs):
        """Retrieve a listing of metadata properties

        :returns generator over list of objects
        """
        url = '/metadefs/namespaces/%s/properties' %(namespace)
        return self._get(url, **kwargs)

    def delete(self, namespace, prop_name, **kwargs):
        """Delete a property."""
        url = '/metadefs/namespaces/%s/properties/%s' %(namespace, prop_name)
        return self._delete(url, **kwargs)

    def delete_all(self, namespace, **kwargs):
        """Delete all properties in a namespace."""
        url = '/metadefs/namespaces/%s/properties' %(namespace)
        return self._delete(url, **kwargs)