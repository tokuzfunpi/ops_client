from ops_client.manager.glance import GlanceBaseManager

class ImageTagManager(GlanceBaseManager):

    def update(self, image_id, tag_value, **kwargs):
        """
        Update an image with the given tag.

        :param image_id:    image to be updated with the given tag.
        :param tag_value:   value of the tag.
        """
        url = '/images/%s/tags/%s' % (image_id, tag_value)
        return self._put(url, **kwargs)

    def delete(self, image_id, tag_value, **kwargs):
        """
        Delete the tag associated with the given image.

        :param image_id:    Image whose tag to be deleted.
        :param tag_value:   tag value to be deleted.
        """
        url = '/images/%s/tags/%s' % (image_id, tag_value)
        return self._delete(url, **kwargs)
