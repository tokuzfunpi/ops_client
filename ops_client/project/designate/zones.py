from ops_client.manager.designate import DesignateBaseManager


class ZoneManager(DesignateBaseManager):

    def list(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones", **kwargs)

    def show(self, zone_id, _type='http', prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/%s" % zone_id, **kwargs)

    def create(self, name, email, ttl=3600, description='', type_='PRIMARY',
               masters=[], prefix='', **kwargs):
        body = {
            "name": name,
            "email": email,
            "ttl": ttl,
            "description": description,
            "type": type_,
            "masters": masters
        }
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._post(prefix+"/zones", body=body, **kwargs)

    def update(self, zone_id, masters=None, email=None, ttl=None,
               description=None, prefix='', **kwargs):
        zone_update = {}
        if masters is not None:
            zone_update['masters'] = masters
        if email is not None:
            zone_update['email'] = email
        if ttl is not None:
            zone_update['ttl'] = ttl
        if description is not None:
            zone_update['description'] = description
        #Support http only
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = zone_update
        return self._patch(prefix+"/zones/%s" % zone_id, body=body, **kwargs)

    def delete(self, zone_id, prefix='', **kwargs):
        return self._delete(prefix+'/zones/%s' % zone_id, **kwargs)

    def abandon(self, zone_id, prefix='', **kwargs):
        body = {}
        return self._post(prefix+"/zones/%s/tasks/abandon" % zone_id, body=body,
                          **kwargs)

    def create_transfer(self, zone_id, target_project_id,
                        description='', prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = {
            "target_project_id": target_project_id,
            "description": description
        }
        return self._post(prefix+"/zones/%s/tasks/transfer_requests" % zone_id,
                          body=body, **kwargs)

    def list_transfer(self, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/tasks/transfer_requests", **kwargs)

    def show_transfer(self, transfer_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(prefix+"/zones/tasks/transfer_requests/%s" % transfer_id,
                         **kwargs)

    def delete_transfer(self, transfer_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._delete(
            prefix+"/zones/tasks/transfer_requests/%s" % transfer_id, **kwargs)

    def show_accept_transfer(self, accept_transfer_id, prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        return self._get(
            prefix+"/zones/tasks/transfer_accepts/%s" % accept_transfer_id,
            **kwargs)

    def accept_transfer(self, zone_transfer_request_id, key,
                        prefix='', **kwargs):
        kwargs['headers'] = self._handle_designate_header(kwargs)
        body = {
            "key": key,
            "zone_transfer_request_id": zone_transfer_request_id
        }
        return self._post(prefix+"/zones/tasks/transfer_accepts",
            body=body, **kwargs)
