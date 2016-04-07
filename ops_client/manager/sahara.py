import six
from six.moves.urllib import parse
from ops_client.manager.base import BaseManager


class SaharaBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'sahara_url'

    def _copy_if_defined(self, data, **kwargs):
        for var_name, var_value in six.iteritems(kwargs):
            if var_value is not None:
                data[var_name] = var_value

    def _parse_query_string(self, search_opts):
        if search_opts:
            qparams = sorted(search_opts.items(), key=lambda x: x[0])
            query_string = "?%s" % parse.urlencode(qparams, doseq=True)
        else:
            query_string = ""

        return query_string
