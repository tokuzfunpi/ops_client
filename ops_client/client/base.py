import urllib
from ops_client.common.request import do_request
from ops_client.common.auth import get_token
import json
import os

class BaseClient():

    def __init__(self,
                 region_name = None,
                 interface = "public",
                 cert = None,
                 timeout = None,
                 **kwargs):
        self.do_request = do_request
        self.interface = interface
        self.region_name = region_name
        self.timeout = timeout
        self.cert = cert
        self.token = None
        self.token_body = None
        self.nova_url = None
        self.glance_url = None
        self.cinder_url = None
        self.manila_url = None
        self.neutron_url = None
        self.ceilometer_url = None
        self.dns_url = None
        self.trove_url = None
        self.heat_url = None
        self.sahara_url = None
        self.user_id = None
        self.project_id = None
        self.user_roles = []
        self.catalogs = []

    def authenticate(self,
                     keystone_url,
                     user_name = None,
                     user_id = None,
                     user_pwd = None,
                     user_domain = None,
                     user_domain_id = None,
                     project_name = None,
                     project_id = None,
                     project_domain = None,
                     project_domain_id = None):
        self.keystone_url = keystone_url
        self.user_name = user_name
        self.user_pwd = user_pwd
        self.user_id = user_id
        self.user_domain = user_domain
        self.user_domain_id = user_domain_id
        self.project_name = project_name
        self.project_id = project_id
        self.project_domain = project_domain
        self.project_domain_id = project_domain_id
        self._authenticate()

    def _authenticate(self) :
        self.token, self.token_body = \
            get_token(url = self.keystone_url,
                      user_name = self.user_name,
                      user_id = self.user_id,
                      user_pwd = self.user_pwd,
                      user_domain = self.user_domain,
                      user_domain_id = self.user_domain_id,
                      project_name = self.project_name,
                      project_id = self.project_id,
                      project_domain = self.project_domain,
                      project_domain_id = self.project_domain_id,
                      version = 'v3')
        self.token_body = self.token_body['token']
        self.user_name = self.token_body.get('user', {}).get('name')
        self.user_id = self.token_body.get('user', {}).get('id')
        _user_domain = self.token_body.get('user', {}).get('domain', {})
        self.user_domain = _user_domain.get('name')
        self.user_domain_id = _user_domain.get('id')
        self.project_id = self.token_body.get('project', {}).get('id', None)
        self.project_name = \
            self.token_body.get('project', {}).get('name', None)
        _project_domain = self.token_body.get('project', {}).get('domain', {})
        self.project_domain = _project_domain.get('name')
        self.project_domain_id = _project_domain.get('id')
        self.user_roles = self.token_body.get('roles', [])
        self.catalogs = self.token_body.get('catalog', [])
        self.parse_endpoints()

    def set_user_token(self, token):
        self.token = token

    def set_service_endpoint(self, endpoint_type, endpoint_url):
        if not endpoint_type in ['compute', 'image', 'volumev2', 'network',
                                 'metering', 'identity', 'dns', 'database',
                                 'orchestration', 'sharev2',
                                 'data-processing'] :
            raise AttributeError("Wrong type of endpoint")
        else :
            if endpoint_type == 'compute' :
                self.nova_url = endpoint_url
            elif endpoint_type == 'image' :
                self.glance_url = endpoint_url
            elif endpoint_type == 'volumev2' :
                self.cinder_url = endpoint_url
            elif endpoint_type == 'sharev2':
                self.manila_url = endpoint_url
            elif endpoint_type == 'network' :
                self.neutron_url = endpoint_url
                #self.neutron_url = \
                #    self.concat_url(endpoint_url, 'v2.0')
            elif endpoint_type == 'metering' :
                self.ceilometer_url = endpoint_url
            elif endpoint_type == 'identity' :
                self.keystone_url = endpoint_url
            elif endpoint_type == 'dns' :
                self.dns_url = endpoint_url
            elif endpoint_type == 'database' :
                self.trove_url = endpoint_url
            elif endpoint_type == 'orchestration' :
                self.heat_url = endpoint_url
            elif endpoint_type == 'data-processing' :
                self.sahara_url = endpoint_url

    def parse_endpoints(self):
        for catalog in self.catalogs :
            _type = catalog.get('type', None)
            if not _type :
                continue
            for endpoint in catalog.get('endpoints', []) :
                if endpoint['interface'] == self.interface :
                    if _type == 'compute' :
                        self.nova_url = endpoint['url']
                    elif _type == 'image' :
                        self.glance_url = endpoint['url']
                    elif _type == 'volumev2' :
                        self.cinder_url = endpoint['url']
                    elif _type == 'sharev2':
                        self.manila_url = endpoint['url']
                    elif _type == 'network' :
                        self.neutron_url = \
                            self.concat_url(endpoint['url'], 'v2.0')
                    elif _type == 'metering' :
                        self.ceilometer_url = \
                            self.concat_url(endpoint['url'], 'v2')
                    elif _type == 'identity' :
                        self.keystone_url = endpoint['url']
                    elif _type == 'dns' :
                        self.dns_url = endpoint['url']
                    elif _type == 'database' :
                        self.trove_url = endpoint['url']
                    elif _type == 'orchestration' :
                        self.heat_url = endpoint['url']
                    elif _type == 'data-processing':
                        self.sahara_url = endpoint['url']

    def join_path(self, *args):
        return os.path.join(*args)

    def serialize(self, kwargs):
        if kwargs.get('json') is not None:
            kwargs['headers']['Content-Type'] = 'application/json'
            kwargs['data'] = json.dumps(kwargs['json'])
        try:
            del kwargs['json']
        except KeyError:
            pass

    @staticmethod
    def concat_url(endpoint, url):
        """Concatenate endpoint and final URL.

        E.g., "http://keystone/v2.0/" and "/tokens" are concatenated to
        "http://keystone/v2.0/tokens".

        :param endpoint: the base URL
        :param url: the final URL
        """
        return "%s/%s" % (endpoint.rstrip("/"), url.strip("/"))

    def quote(self, name):
        return urllib.quote(name)

    def add_query_string(self, url, param):
        new_param = {}
        for k, v in param.items() :
            if v == None : continue
            if type(v) == unicode :
                new_param[k] = v.encode('utf-8')
            else :
                new_param[k] = v
        param = new_param
        _param = urllib.urlencode(param)
        _url = url.endswith('&') and (url + _param) or (url + '?' + _param)
        return _url
