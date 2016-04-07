import six
from six.moves.urllib import parse
from oslo_utils import encodeutils
from ops_client.manager.glance import GlanceBaseManager

DEFAULT_PAGE_SIZE = 20
SORT_DIR_VALUES = ('asc', 'desc')
SORT_KEY_VALUES = ('created_at', 'namespace')

class MetaDefNamespaceManager(GlanceBaseManager):

    def create(self, name, extra_body = {}, **kwargs):
        """Create a namespace.

        :param kwargs: Unpacked namespace object.
        """
        url = '/metadefs/namespaces'
        body = extra_body
        body['namespace'] = name
        return self._post(url, body = body, **kwargs)

    def update(self, namespace, new_name, extra_body = {}, **kwargs):
        """Update a namespace.

        :param namespace_name: Name of a namespace (old one).
        :param kwargs: Unpacked namespace object.
        """
        
        url = '/metadefs/namespaces/%s' %(namespace)
        body = extra_body
        body['namespace'] = new_name
        return self._put(url, body = body, **kwargs)

    def get(self, namespace, query = {}, **kwargs):
        """Get one namespace."""
        query_params = parse.urlencode(query)
        if query:
            query_params = '?%s' % query_params

        url = '/metadefs/namespaces/%s%s' %(namespace, query_params)
        return self._get(url, **kwargs)

    def list(self, filters = None, page_size = None, marker = None, 
             sort_key = None, sort_dir = None, **kwargs):
        """Retrieve a listing of Namespace objects
        :param page_size: Number of items to request in each paginated request
        :param limit: Use to request a specific page size. Expect a response
                      to a limited request to return between zero and limit
                      items.
        :param marker: Specifies the namespace of the last-seen namespace.
                       The typical pattern of limit and marker is to make an
                       initial limited request and then to use the last
                       namespace from the response as the marker parameter
                       in a subsequent limited request.
        :param sort_key: The field to sort on (for example, 'created_at')
        :param sort_dir: The direction to sort ('asc' or 'desc')
        :returns generator over list of Namespaces
        """

        filters = {} if filters is None else filters
        if page_size:
            try:
                int(page_size)
            except:
                raise ValueError('limit must be an integer')
            filters['limit'] = page_size
        else:
            filters['limit'] = DEFAULT_PAGE_SIZE

        if marker:
            filters['marker'] = marker

        if sort_key is not None:
            if sort_key in SORT_KEY_VALUES:
                filters['sort_key'] = sort_key
            else:
                raise ValueError('sort_key must be one of the following: %s.'
                                 % ', '.join(SORT_KEY_VALUES))

        if sort_dir is not None:
            if sort_dir in SORT_DIR_VALUES:
                filters['sort_dir'] = sort_dir
            else:
                raise ValueError('sort_dir must be one of the following: %s.'
                                 % ', '.join(SORT_DIR_VALUES))

        for param, value in six.iteritems(filters):
            if isinstance(value, list):
                filters[param] = encodeutils.safe_encode(','.join(value))
            elif isinstance(value, six.string_types):
                filters[param] = encodeutils.safe_encode(value)

        url = '/metadefs/namespaces?%s' % parse.urlencode(filters)

        return self._get(url, **kwargs)

    def delete(self, namespace, **kwargs):
        """Delete a namespace."""
        url = '/metadefs/namespaces/%s' %(namespace)
        return self._delete(url, **kwargs)