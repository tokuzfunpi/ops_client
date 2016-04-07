from ops_client.manager.glance import GlanceBaseManager

class MetaDefResourceTypeManager(GlanceBaseManager):

    def associate(self, namespace, res_type = {}, **kwargs):
        """Associate a resource type with a namespace."""
        body = res_type
        url = '/metadefs/namespaces/%s/resource_types' %(namespace)
        return self._post(url, body = body, **kwargs)

    def deassociate(self, namespace, res_type, **kwargs):
        """Deasociate a resource type with a namespace."""
        url = '/metadefs/namespaces/%s/resource_types/%s' %(namespace, res_type)
        return self._delete(url)

    def list(self, **kwargs):
        """Retrieve a listing of available resource types

        :returns generator over list of resource_types
        """
        url = '/metadefs/resource_types'
        return self._get(url, **kwargs)

    def get(self, namespace, **kwargs):
        url = '/metadefs/namespaces/%s/resource_types' %(namespace)
        return self._get(url, **kwargs)
