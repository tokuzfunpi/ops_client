"""
Quota Classes interface. (Unknown usage about this module)
"""

from ops_client.manager.nova import NovaBaseManager

class QuotaClassSetManager(NovaBaseManager):

    def get(self, class_name, response_key = True, **kwargs):
        if response_key :
            return self._get("/os-quota-class-sets/%s" % (class_name),
                             "quota_class_set", **kwargs)
        else :
            return self._get("/os-quota-class-sets/%s" % (class_name), **kwargs)

    def _update_body(self, quota_body):
        return {'quota_class_set': quota_body}

    def update(self, class_name, 
               quota_body = None, response_key = True, **kwargs):
        if quota_body and type(quota_body) == dict :
            body = self._update_body(quota_body)

        for key in list(body['quota_class_set']):
            if body['quota_class_set'][key] is None:
                body['quota_class_set'].pop(key)

        if response_key :
            return self._put('/os-quota-class-sets/%s' % (class_name),
                                body, 'quota_class_set', **kwargs)
        else :
            return self._put('/os-quota-class-sets/%s' % (class_name),
                                body, **kwargs)
