from ops_client.manager.designate import DesignateBaseManager

class BlackListManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/blacklists", **kwargs)

    def show(self, blacklist_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/blacklists/%s" % blacklist_id, **kwargs)

    def create(self, pattern, description = '', prefix='', **kwargs):
        body = {
            "pattern": pattern,
            "description": description
        }
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._post(prefix+"/blacklists", body = body, **kwargs)
    
    def update(self, blacklist_id, pattern = None, description = None, 
               prefix='', **kwargs):
        blacklist_update = {}
        if pattern is not None :
            blacklist_update['pattern'] = pattern
        if description is not None :
            blacklist_update['description'] = description
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = blacklist_update

        return self._patch(prefix+"/blacklists/%s" % blacklist_id, body = body, 
                           **kwargs)

    def delete(self, blacklist_id, prefix='', **kwargs):
        return self._delete(prefix+'/blacklists/%s' % blacklist_id,
                            **kwargs)
