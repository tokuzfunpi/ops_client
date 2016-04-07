from ops_client.manager.base import BaseManager
from six.moves import urllib

class CeilometerBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'ceilometer_url'

    def build_url(self, path, q, params=None):
        if q:
            if type(q) == list :
                query_params = {'q.field': [],
                                'q.value': [],
                                'q.op': [],
                                'q.type': []}

                for query in q:
                    # print q
                    for name in ['field', 'op', 'value', 'type']:
                        query_params['q.%s' % name].append(query.get(name, ''))

                # Transform the dict to a sequence of two-element tuples in fixed
                # order, then the encoded string will be consistent in Python 2&3.
                new_qparams = sorted(query_params.items(), key=lambda x: x[0])
                path += "?" + urllib.parse.urlencode(new_qparams, doseq=True)
            elif type(q) == str:
                path += "?" + q
            if params:
                for p in params:
                    path += '&%s' % p
        elif params:
            path += '?%s' % params[0]
            for p in params[1:]:
                path += '&%s' % p
        return path
