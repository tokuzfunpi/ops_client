from ops_client.manager.designate import DesignateBaseManager

class PoolManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/pools", **kwargs)

    def show(self, pool_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/pools/%s" % pool_id, **kwargs)

    def create(self, name, ns_records=[], attributes={},
               description="", prefix='', **kwargs):
        body = {
            "name": name,
            "ns_records": ns_records,
            "attributes": attributes,
            "description": description
        }
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._post(prefix+"/pools", body=body, **kwargs)

    # def update(self, pool_id, nameservers, **kwargs):
    def update(self, pool_id, name="", ns_records=[], attributes={},
               description="", prefix='', **kwargs):
        pool_update = {}

        if name:
            pool_update['name'] = name
        if ns_records:
            pool_update['ns_records'] = ns_records
        if attributes:
            pool_update['attributes'] = attributes
        if description:
            pool_update['description'] = description


        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = pool_update

        return self._patch(prefix+"/pools/%s" % pool_id, body = body, **kwargs)

    def delete(self, pool_id, prefix='', **kwargs):
        return self._delete(prefix+'/pools/%s' % pool_id, **kwargs)
