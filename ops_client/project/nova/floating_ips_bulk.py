"""
Bulk Floating IPs interface.
"""

from ops_client.manager.nova import NovaBaseManager

class FloatingIPBulkManager(NovaBaseManager):

    def list(self, host=None, response_key = True, **kwargs):
        """
        List all floating IPs
        """
        if host is None:
            if response_key :
                return self._get('/os-floating-ips-bulk',
                                 'floating_ip_info', **kwargs)
            else:
                return self._get('/os-floating-ips-bulk', **kwargs)
        else:
            if response_key :
                return self._get('/os-floating-ips-bulk/%s' % host,
                                  'floating_ip_info', **kwargs)
            else :
                return self._get('/os-floating-ips-bulk/%s' % host, **kwargs)

    def create(self, ip_range, pool=None, interface=None,
               response_key = True, **kwargs):
        """
        Create floating IPs by range
        """
        body = {"floating_ips_bulk_create": {'ip_range': ip_range}}
        if pool is not None:
            body['floating_ips_bulk_create']['pool'] = pool
        if interface is not None:
            body['floating_ips_bulk_create']['interface'] = interface

        if response_key :
            return self._post('/os-floating-ips-bulk', body,
                                'floating_ips_bulk_create', **kwargs)
        else :
            return self._post('/os-floating-ips-bulk', body, **kwargs)

    def delete(self, ip_range, **kwargs):
        """
        Delete floating IPs by range
        """
        body = {"ip_range": ip_range}
        return self._update('/os-floating-ips-bulk/delete', body, **kwargs)
