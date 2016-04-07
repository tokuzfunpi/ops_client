"""
Keypair interface.
"""

from ops_client.manager.nova import NovaBaseManager

class KeypairManager(NovaBaseManager):

    def get(self, keypair_name, response_key = True, **kwargs):
        """
        Get a keypair.

        :param keypair: The ID of the keypair to get.
        :rtype: :class:`Keypair`
        """
        if response_key :
            return self._get("/os-keypairs/%s" % keypair_name,
                             "keypair", **kwargs)
        else :
            return self._get("/os-keypairs/%s" % keypair_name, **kwargs)

    def create(self, name, public_key=None, response_key = True, **kwargs):
        """
        Create a keypair

        :param name: name for the keypair to create
        :param public_key: existing public key to import
        """
        body = {'keypair': {'name': name}}
        if public_key:
            body['keypair']['public_key'] = public_key
        if response_key :
            return self._post('/os-keypairs', body, 'keypair', **kwargs)
        else :
            return self._post('/os-keypairs', body, **kwargs)

    def delete(self, keypair_name, **kwargs):
        """
        Delete a keypair

        :param key: The :class:`Keypair` (or its ID) to delete.
        """
        return self._delete('/os-keypairs/%s' % keypair_name, **kwargs)

    def list(self, response_key = True, **kwargs):
        """
        Get a list of keypairs.
        """
        if response_key :
            return self._get('/os-keypairs', 'keypairs', **kwargs)
        else :
            return self._get('/os-keypairs', **kwargs)
