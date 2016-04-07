from ops_client.manager.glance import GlanceBaseManager

class MetaDefObjectManager(GlanceBaseManager):

    def create(self, namespace, name, extra_body = {}, **kwargs):
        """Create an object.

        :param namespace: Name of a namespace the object belongs.
        :param kwargs: Unpacked object.
        """
        body = extra_body
        body['name'] = name
        url = '/metadefs/namespaces/%s/objects' %(namespace)
        return self._post(url, body = body, **kwargs)

    def update(self, namespace, object_name, new_name, extra_body = {}, **kwargs):
        """Update an object.

        :param namespace: Name of a namespace the object belongs.
        :param prop_name: Name of an object (old one).
        :param kwargs: Unpacked object.
        """
        body = extra_body
        body['name'] = new_name
        url = '/metadefs/namespaces/%s/objects/%s' %(namespace, object_name)
        return self._put(url, body = body, **kwargs)

    def get(self, namespace, object_name, **kwargs):
        url = '/metadefs/namespaces/%s/objects/%s' %(namespace, object_name)
        return self._get(url, **kwargs)

    def list(self, namespace, **kwargs):
        """Retrieve a listing of metadata objects

        :returns generator over list of objects
        """
        url = '/metadefs/namespaces/%s/objects' %(namespace)
        return self._get(url, **kwargs)

    def delete(self, namespace, object_name, **kwargs):
        """Delete an object."""
        url = '/metadefs/namespaces/%s/objects/%s' %(namespace, object_name)
        return self._delete(url, **kwargs)

    def delete_all(self, namespace, **kwargs):
        """Delete all objects in a namespace."""
        url = '/metadefs/namespaces/%s/objects' %(namespace)
        return self._delete(url, **kwargs)