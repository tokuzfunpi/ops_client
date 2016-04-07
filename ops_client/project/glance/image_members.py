from ops_client.manager.glance import GlanceBaseManager

class ImageMemberManager(GlanceBaseManager):

    def list(self, image_id, **kwargs):
        """
        Retrieve a listing of Image members

        :param image_id: ID of the image. (uuid)
        :returns: generator over list of Image members
        """
        url = '/images/%s/members' % image_id
        return self._get(url, **kwargs)

    def delete(self, image_id, member_id, **kwargs):
        """Delete an image member."""
        return self._delete('/images/%s/members/%s' % (image_id, member_id),
                            **kwargs)

    def update(self, image_id, member_id, member_status, **kwargs):
        """
        Update attributes of an image member.

        :param image_id: ID of the image. (uuid)
        :param member_id: ID of the member. (uuid)
        :param member_status: Status of the member. (string)
        """
        url = '/images/%s/members/%s' % (image_id, member_id)
        body = {'status': member_status}
        return self._put(url, body = body, **kwargs)

    def create(self, image_id, user_id, **kwargs):
        """Create an image member.

        :param image_id: ID of the image. (uuid)
        :param user_id: ID of the user. (uuid)
        """
        url = '/images/%s/members' % image_id
        body = {'member': user_id}
        return self._post(url, body = body, **kwargs)
