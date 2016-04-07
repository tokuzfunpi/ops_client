from ops_client.manager.trove import TroveBaseManager

class MetadataManager(TroveBaseManager):

    def list(self, instance_id, response_key = True, **kwargs):
        if response_key :
            return self._get('/instances/%s/metadata' % instance_id,
                             'metadata', **kwargs)
        else :
            return self._get('/instances/%s/metadata' % instance_id, **kwargs)

    def show(self, instance_id, key, response_key = True, **kwargs):
        if response_key :
            return self._get('/instances/%s/metadata/%s' % (instance_id, key),
                             'metadata', **kwargs)
        else :
            return self._get('/instances/%s/metadata/%s' % (instance_id, key),
                             **kwargs)

    def create(self, instance_id, key, value, response_key = True, **kwargs):
        body = {
            'metadata': {
                'value': value
            }
        }
        if response_key :
            return self._post('/instances/%s/metadata/%s' % (instance_id, key),
                              body, 'metadata', **kwargs)
        else :
            return self._post('/instances/%s/metadata/%s' % (instance_id, key),
                              body, **kwargs)

    def update(self, instance_id, key, newkey, value, **kwargs):
        body = {
            'metadata': {
                'key': newkey,
                'value': value
            }
        }
        return self._put('/instances/%s/metadata/%s' % (instance_id, key),
                         body, **kwargs)

    def edit(self, instance_id, key, value, **kwargs):
        body = {
            'metadata': {
                'value': value
            }
        }
        return self._patch('/instances/%s/metadata/%s' % (instance_id, key),
                           body, **kwargs)

    def delete(self, instance_id, key, **kwargs):
        return self._delete('/instances/%s/metadata/%s' % (instance_id, key),
                            **kwargs)