"""
Certificate interface.
"""

from ops_client.manager.nova import NovaBaseManager

# Did not test because we don't use cert currently.
class CertificateManager(NovaBaseManager):

    def create(self, response_key = True, **kwargs):
        """
        Create a x509 certificate for a user in tenant.
        """
        if response_key :
            return self._post('/os-certificates', {}, 'certificate', **kwargs)
        else :
            return self._post('/os-certificates', {}, **kwargs)

    def get(self, response_key = True, **kwargs):
        """
        Get root certificate.
        """
        if response_key :
            return self._get("/os-certificates/root", 'certificate', **kwargs)
        else :
            return self._get("/os-certificates/root", **kwargs)
