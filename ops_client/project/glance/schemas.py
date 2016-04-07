from ops_client.manager.glance import GlanceBaseManager

class SchemaManager(GlanceBaseManager):

    def get(self, schema_name):
        uri = '/schemas/%s' % schema_name
        return self._get(uri)
