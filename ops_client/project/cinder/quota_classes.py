from ops_client.manager.cinder import CinderBaseManager

class QuotaClassSetManager(CinderBaseManager):

    def get(self, class_name, **kwargs):
        return self._get("/os-quota-class-sets/%s" % (class_name), **kwargs)

    def update(self, class_name, updates = None, **kwargs):
        body = {'quota_class_set': {'class_name': class_name}}

        if not updates:
            return
            
        for update in updates:
            body['quota_class_set'][update] = updates[update]

        return self._put('/os-quota-class-sets/%s' % (class_name), 
                         body = body, **kwargs)
