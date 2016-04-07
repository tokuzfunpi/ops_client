import six
from six.moves.urllib import parse
from ops_client.common import strutils
from ops_client.common.utils import integrity_iter
from ops_client.manager.glance import GlanceBaseManager
from ops_client.common.exception import BadRequest, Conflict, NotFound

DEFAULT_LIMIT = 50
VALID_OPS = ['replace', 'add', 'remove']

class ImageManager(GlanceBaseManager):

    def list(self, filters = {}, limit = DEFAULT_LIMIT, tags = [], **kwargs):
        """
        Retrieve a listing of Image objects

        :param page_size: Number of images to request in each paginated request
        :returns: generator over list of Images
        """

        filters['limit'] = limit
        tags_url_params = []
        for tag in tags:
            if isinstance(tag, six.string_types):
                tags_url_params.append({'tag': strutils.safe_encode(tag)})

        for param, value in six.iteritems(filters):
            if isinstance(value, six.string_types):
                filters[param] = strutils.safe_encode(value)

        url = '/images?%s' % parse.urlencode(filters)
        for param in tags_url_params:
            url = '%s&%s' % (url, parse.urlencode(param))
        return self._get(url, **kwargs)

    def get(self, image_id, **kwargs):
        return self._get('/images/%s' % image_id, **kwargs)

    def data(self, image_id, do_checksum = True, **kwargs):
        """
        Retrieve data of an image.

        :param image_id:    ID of the image to download.
        :param do_checksum: Enable/disable checksum validation.
        """
        kwargs['read'] = False
        kwargs['response_key'] = False
        kwargs['json_parse'] = False

        resp, body = self._get('/images/%s/file' % image_id, **kwargs)
        checksum = resp.headers.get('content-md5', None)

        if do_checksum and checksum is not None:
            return resp, integrity_iter(body, checksum)
        else:
            return resp, body

    def upload(self, image_id, image_data = None, image_size = None, 
               timeout = 600, raw_body = None, **kwargs):
        """
        Upload the data for an image.

        :param image_id: ID of the image to upload data for.
        :param image_data: File-like object supplying the data to upload.
        :param image_size: Total size in bytes of image to be uploaded.
        """
        url = '/images/%s/file' % image_id
        content_type = 'application/octet-stream'

        if image_size and not raw_body :
            body = {'image_data': image_data,
                    'image_size': image_size}
        elif raw_body :
            body = raw_body
        else:
            body = image_data

        return self._put(url, body = body, 
                         timeout = timeout,
                         content_size = image_size, 
                         content_type = content_type, **kwargs)

    def delete(self, image_id, **kwargs):
        """Delete an image."""
        return self._delete('/images/%s' % image_id, **kwargs)

    def create(self, image_name, disk_format, container_format,
               visibility = 'private', tags = None, image_type = None,
               extra_body = {},  **kwargs):
        """Create an image.

        :param image_name: Name of the image to create. (string)
        :param image_type: Type of the image. (string)
        :param disk_format: Disk format of the image. (string)
        :param container_format: Container Format of the image. (string)
        """
        body = extra_body
        body['name'] = image_name
        body['type'] = image_type or ''
        body['disk_format'] = disk_format
        body['container_format'] = container_format
        body['tags'] = tags or []
        body['visibility'] = visibility
        return self._post('/images', body = body, **kwargs)

    def update(self, image_id, body = [], **kwargs):
        """
        Update attributes of an image.

        :param image_id: ID of the image to modify.
        :param remove_props: List of property names to remove
        :param **kwargs: Image attribute names and their new values.
        """
        url = '/images/%s' % image_id
        content_type='application/openstack-images-v2.1-json-patch'
        if type(body) is list:
            _body = []
            for _k in body:
                if not "op" in _k and not "path" in _k:
                    raise KeyError("Dict Keys should both have 'op' and 'path'")
                else:
                    if not _k["op"] in VALID_OPS:
                        msg = "'op' must be one of %s"
                        msg = msg % ', '.join(VALID_OPS)
                        raise ValueError(msg)
                    if _k["op"] == "add" or _k["op"] == "replace":
                        if "value" in _k:
                            _body.append(_k)
                        else:
                            raise KeyError(
                                "Dict Keys should both have and 'value'")
                    elif _k["op"] == "remove":
                        _body.append(_k)                 
        else:
            raise TypeError("Body should be a list.")
        return self._patch(url, body = _body, 
                           content_type = content_type, **kwargs)

    def _get_image_with_locations_or_fail(self, image_id, **kwargs):
        resp, image = self.get(image_id)
        if not image.get('locations') :
            raise BadRequest(message ='The administrator has disabled '
                                      'API access to image locations')
        return image

    def _send_image_update_request(self, image_id, patch_body, **kwargs):
        url = '/images/%s' % image_id
        hdrs = {'Content-Type': 'application/openstack-images-v2.1-json-patch'}
        return self._patch(url, headers = hdrs, body = patch_body, **kwargs)

    def add_location(self, image_id, url, metadata, **kwargs):
        """Add a new location entry to an image's list of locations.

        It is an error to add a URL that is already present in the list of
        locations.

        :param image_id: ID of image to which the location is to be added.
        :param url: URL of the location to add.
        :param metadata: Metadata associated with the location.
        :returns: The updated image
        """
        image = self._get_image_with_locations_or_fail(image_id)
        url_list = [l['url'] for l in image['locations']]
        if url in url_list:
            err_str = 'A location entry at %s already exists' % url
            raise Conflict(message = err_str)

        add_patch = [{'op': 'add', 'path': '/locations/-',
                      'value': {'url': url, 'metadata': metadata}}]
        self._send_image_update_request(image_id, add_patch)
        return self.get(image_id, **kwargs)

    def delete_locations(self, image_id, url_set, **kwargs):
        """Remove one or more location entries of an image.

        :param image_id: ID of image from which locations are to be removed.
        :param url_set: set of URLs of location entries to remove.
        :returns: None
        """
        image = self._get_image_with_locations_or_fail(image_id)
        current_urls = [l['url'] for l in image.locations]

        missing_locs = url_set.difference(set(current_urls))
        if missing_locs:
            raise NotFound(message = 'Unknown URL(s): %s' % list(missing_locs))

        # NOTE: warlock doesn't generate the most efficient patch for remove
        # operations (it shifts everything up and deletes the tail elements) so
        # we do it ourselves.
        url_indices = [current_urls.index(url) for url in url_set]
        url_indices.sort(reverse=True)
        patches = [{'op': 'remove', 'path': '/locations/%s' % url_idx}
                   for url_idx in url_indices]
        return self._send_image_update_request(image_id, patches, **kwargs)

    def update_location(self, image_id, url, metadata, **kwargs):
        """Update an existing location entry in an image's list of locations.

        The URL specified must be already present in the image's list of
        locations.

        :param image_id: ID of image whose location is to be updated.
        :param url: URL of the location to update.
        :param metadata: Metadata associated with the location.
        :returns: The updated image
        """
        image = self._get_image_with_locations_or_fail(image_id)
        url_map = dict([(l['url'], l) for l in image.locations])
        if url not in url_map:
            raise NotFound(message = 'Unknown URL: %s' % url)

        if url_map[url]['metadata'] == metadata:
            return self.get(image_id, **kwargs)

        # NOTE: The server (as of now) doesn't support modifying individual
        # location entries. So we must:
        #   1. Empty existing list of locations.
        #   2. Send another request to set 'locations' to the new list
        #      of locations.
        url_map[url]['metadata'] = metadata
        patches = [{'op': 'replace',
                    'path': '/locations',
                    'value': p} for p in ([], list(url_map.values()))]
        self._send_image_update_request(image_id, patches)

        return self.get(image_id, **kwargs)
