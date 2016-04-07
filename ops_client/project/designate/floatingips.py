from ops_client.manager.designate import DesignateBaseManager

class FloatingIPManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/reverse/floatingips", **kwargs)

    def show(self, ptr_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/reverse/floatingips/%s" % ptr_id, **kwargs)

    def update(self, ptr_id, ptrdname = None, description = None, 
               prefix='', **kwargs):
        floatingip_update = {}
        if ptrdname is not None :
            floatingip_update['ptrdname'] = ptrdname
        if description is not None :
            floatingip_update['description'] = description
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = {
            "floatingip" : floatingip_update
        }
        return self._patch(prefix+"/reverse/floatingips/%s" % ptr_id, body = body, 
                           **kwargs)
