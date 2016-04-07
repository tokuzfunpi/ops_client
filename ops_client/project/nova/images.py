"""
Image interface.
"""

from ops_client.manager.nova import NovaBaseManager

class ImageManager(NovaBaseManager):

    def get(self, image_id, response_key = True, **kwargs):
        """
        Get an image.

        :param image: The ID of the image to get.
        :rtype: :class:`Image`
        """
        if response_key :
            return self._get("/images/%s" % image_id, "image", **kwargs)
        else :
            return self._get("/images/%s" % image_id, **kwargs)

    def list(self, detailed=True, params = None, response_key = True, **kwargs):
        """
        Get a list of all images.

        :rtype: list of :class:`Image`
        :param limit: maximum number of images to return.
        """
        detail = ''
        if detailed:
            detail = '/detail'
        if response_key :
            return self._get('/images%s' % detail, 'images', **kwargs)
        else :
            return self._get('/images%s' % detail, **kwargs)

    def delete(self, image_id, **kwargs):
        """
        Delete an image.

        It should go without saying that you can't delete an image
        that you didn't create.

        :param image: The :class:`Image` (or its ID) to delete.
        """
        return self._delete("/images/%s" % image_id, **kwargs)

    def set_meta(self, image_id, metadata, response_key = True, **kwargs):
        """
        Set an images metadata

        :param image: The :class:`Image` to add metadata to
        :param metadata: A dict of metadata to add to the image
        """
        if type(metadata) is dict:
            body = {'metadata': metadata}
            if response_key :
                return self._post("/images/%s/metadata" % image_id, body,
                                     "metadata", **kwargs)
            else :
                return self._post("/images/%s/metadata" % image_id, body,
                                     **kwargs)
        else:
            raise TypeError('Metadata Type should be dict.')

    def delete_meta(self, image_id, keys, **kwargs):
        """
        Delete metadata from an image

        :param image: The :class:`Image` to delete metadata
        :param keys: A list of metadata keys to delete from the image
        """
        if type(keys) is list:
            for k in keys:
                return self._delete("/images/%s/metadata/%s" % (image_id, k),
                                    **kwargs)
        else:
            raise TypeError('Keys Type should be list.')
