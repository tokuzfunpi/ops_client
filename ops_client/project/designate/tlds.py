from ops_client.manager.designate import DesignateBaseManager

class TldManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/tlds", **kwargs)

    def show(self, tld_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/tlds/%s" % tld_id, **kwargs)

    def create(self, name, description = '', prefix='', **kwargs):
        body = {
            "name": name,
            "description": description
        }
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._post(prefix+"/tlds", body = body, **kwargs)
    
    def update(self, tld_id, name = None, description = None, prefix='',
               **kwargs):
        tld_update = {}
        if name is not None :
            tld_update['name'] = name
        if description is not None :
            tld_update['description'] = description
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = tld_update

        return self._patch(prefix+"/tlds/%s" % tld_id, body = body, **kwargs)

    def delete(self, tld_id, prefix='', **kwargs):
        return self._delete(prefix+'/tlds/%s' % tld_id, **kwargs)
