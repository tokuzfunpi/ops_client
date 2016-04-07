from ops_client.manager.sahara import SaharaBaseManager


class ImageManager(SaharaBaseManager):

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/images%s' % query_string
        return self._get(url, **kwargs)

    def get(self, image_id, **kwargs):
        url = '/images/%s' % image_id
        return self._get(url, **kwargs)

    def unregister_image(self, image_id, **kwargs):
        url = '/images/%s' % image_id
        return self._delete(url, **kwargs)

    def register_image(self, image_id, user_name, desc, **kwargs):
        body = {"username": user_name,
                "description": desc}
        url = '/images/%s' % image_id

        return self._post(url, body, **kwargs)

    def add_tags(self, image_id, new_tags, **kwargs):
        if type(new_tags) is not list:
            raise TypeError('Add tags should be a list.')
        body = {
            'tags': new_tags
        }
        url = '/images/%s/tag' % image_id
        return self._post(url, body, **kwargs)

    def remove_tag(self, image_id, remove_tags, **kwargs):
        if type(remove_tags) is not list:
            raise TypeError('Remove tags should be a list.')
        body = {
            'tags': remove_tags
        }
        url = '/images/%s/untag' % image_id
        return self._post(url, body, **kwargs)
