from ops_client.manager.manila import ManilaBaseManager
from ops_client.common import manila_constants as constants

import collections
# import re
try:
    from urllib import urlencode  # noqa
except ImportError:
    from urllib.parse import urlencode  # noqa

RESOURCES_PATH = '/security-services'
RESOURCE_PATH = "/security-services/%s"
RESOURCE_NAME = 'security_service'
RESOURCES_NAME = 'security_services'


class SecurityServiceManager(ManilaBaseManager):
    """Manage :class:`SecurityService` resources."""

    def create(self, type, dns_ip=None, server=None, domain=None, user=None,
               password=None, name=None, description=None):
        """Create security service for NAS.

        :param type: security service type - 'ldap', 'kerberos' or
                     'active_directory'
        :param dns_ip: dns ip address used inside tenant's network
        :param server: security service server ip address or hostname
        :param domain: security service domain
        :param user: security identifier used by tenant
        :param password: password used by user
        :param name: security service name
        :param description: security service description
        :rtype: :class:`SecurityService`
        """
        values = {'type': type}
        if dns_ip:
            values['dns_ip'] = dns_ip
        if server:
            values['server'] = server
        if domain:
            values['domain'] = domain
        if user:
            values['user'] = user
        if password:
            values['password'] = password
        if name:
            values['name'] = name
        if description:
            values['description'] = description

        body = {RESOURCE_NAME: values}

        return self._create(RESOURCES_PATH, body, RESOURCE_NAME)

    def get(self, security_service):
        """Get a security service info.

        :param security_service: security service to get.
        :rtype: :class:`SecurityService`
        """
        return self._get(
            RESOURCE_PATH % common_base.getid(security_service),
            RESOURCE_NAME,
        )

    def update(self, security_service, dns_ip=None, server=None, domain=None,
               password=None, user=None, name=None, description=None):
        """Updates a security service.

        :param security_service: security service to update.
        :param dns_ip: dns ip address used inside tenant's network
        :param server: security service server ip address or hostname
        :param domain: security service domain
        :param user: security identifier used by tenant
        :param password: password used by user
        :param name: security service name
        :param description: security service description
        :rtype: :class:`SecurityService`
        """

        values = {}
        if dns_ip is not None:
            values['dns_ip'] = dns_ip
        if server is not None:
            values['server'] = server
        if domain is not None:
            values['domain'] = domain
        if user is not None:
            values['user'] = user
        if password is not None:
            values['password'] = password
        if name is not None:
            values['name'] = name
        if description is not None:
            values['description'] = description

        for k, v in six.iteritems(values):
            if v == '':
                values[k] = None

        if not values:
            msg = "Must specify fields to be updated"
            raise exceptions.CommandError(msg)

        body = {RESOURCE_NAME: values}

        return self._update(
            RESOURCE_PATH % common_base.getid(security_service),
            body,
            RESOURCE_NAME,
        )

    def delete(self, security_service):
        """Delete a security service.

        :param security_service: security service to be deleted.
        """
        self._delete(RESOURCE_PATH % common_base.getid(security_service))

    def list(self, detailed=True, search_opts=None, **kwargs):
        """Get a list of all security services.

        :rtype: list of :class:`SecurityService`
        """
        if search_opts:
            query_string = urlencode(
                sorted([(k, v) for (k, v) in list(search_opts.items()) if v]))
            if query_string:
                query_string = "?%s" % query_string
        else:
            query_string = ''

        if detailed:
            path = RESOURCES_PATH + "/detail" + query_string
        else:
            path = RESOURCES_PATH + query_string

        return self._get(path, **kwargs)
