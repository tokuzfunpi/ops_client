from ops_client.manager.designate import DesignateBaseManager


class RecordSetManager(DesignateBaseManager):

    def list(self, zone_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/%s/recordsets" % zone_id, **kwargs)

    def show(self, zone_id, recordset_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/%s/recordsets/%s" % (zone_id, recordset_id),
                         **kwargs)

    def create(self, zone_id, name, _type, ttl=3600, description='',
               records=[], prefix='', **kwargs):
        body = {
            "name": name,
            "type": _type,
            "ttl": ttl,
            "description": description,
            "records": records
        }
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._post(prefix+"/zones/%s/recordsets" % zone_id, body=body,
                          **kwargs)

    def update(self, zone_id, recordset_id, ttl=None,
               description=None, records=None, prefix='', **kwargs):
        recordset_update = {}
        if ttl is not None:
            recordset_update['ttl'] = ttl
        if description is not None:
            recordset_update['description'] = description
        if records is not None and type(records) == list:
            recordset_update['records'] = records
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = recordset_update
        return self._put(
            prefix+"/zones/%s/recordsets/%s" % (zone_id, recordset_id),
            body=body, **kwargs)

    def delete(self, zone_id, recordset_id, prefix='', **kwargs):
        return self._delete(
            prefix+'/zones/%s/recordsets/%s' % (zone_id, recordset_id),
            **kwargs)
