from ops_client.manager.base import BaseManager
from ops_client.common.exception import NoUniqueMatch
import urllib
import functools

def getid(obj):
    """
    Abstracts the common pattern of allowing both an object or an object's ID
    (UUID) as a parameter when dealing with relationships.
    """

    # Try to return the object's UUID first, if we have a UUID.
    try:
        if obj.uuid:
            return obj.uuid
    except AttributeError:
        pass
    try:
        return obj.id
    except AttributeError:
        return obj


def filter_kwargs(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        for key, ref in kwargs.items():
            if ref is None:
                # drop null values
                del kwargs[key]
                continue

            id_value = getid(ref)
            if id_value == ref:
                continue

            # if an object with an id was passed remove the object
            # from params and replace it with just the id.
            # e.g user: User(id=1) becomes user_id: 1
            del kwargs[key]
            kwargs['%s_id' % key] = id_value

        return f(*args, **kwargs)
    return func

class KeystoneBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'keystone_url'

    def build_url(self, dict_args_in_out=None):
        """Builds a resource URL for the given kwargs.

        Given an example collection where `collection_key = 'entities'` and
        `key = 'entity'`, the following URL's could be generated.

        By default, the URL will represent a collection of entities, e.g.::

            /entities

        If kwargs contains an `entity_id`, then the URL will represent a
        specific member, e.g.::

            /entities/{entity_id}

        If a `base_url` is provided, the generated URL will be appended to it.

        """
        if dict_args_in_out is None:
            dict_args_in_out = {}

        url = dict_args_in_out.pop('base_url', None) or ''
        url += '/%s' % self.collection_key

        # do we have a specific entity?
        entity_id = dict_args_in_out.pop('%s_id' % self.key, None)
        if entity_id is not None:
            url += '/%s' % entity_id

        return url

    @filter_kwargs
    def create(self, **kwargs):
        url = self.build_url(dict_args_in_out=kwargs)
        return self._post(
            url,
            body = {self.key: kwargs},
            response_key = self.key)

    @filter_kwargs
    def get(self, **kwargs):
        return self._get(
            self.build_url(dict_args_in_out=kwargs),
            response_key = self.key)

    @filter_kwargs
    def head(self, **kwargs):
        return self._head(self.build_url(dict_args_in_out=kwargs))

    @filter_kwargs
    def list(self, **kwargs):
        url = self.build_url(dict_args_in_out=kwargs)

        return self._get(
            '%(url)s%(query)s' % {
                'url': url,
                'query': '?%s' % urllib.urlencode(kwargs) if kwargs else '',
            },
            response_key = self.collection_key)

    @filter_kwargs
    def put(self, **kwargs):
        return self._put(
            self.build_url(dict_args_in_out=kwargs))

    @filter_kwargs
    def update(self, **kwargs):
        url = self.build_url(dict_args_in_out=kwargs)

        return self._patch(
            url,
            body = {self.key: kwargs},
            response_key = self.key)

    @filter_kwargs
    def delete(self, **kwargs):
        return self._delete(
            self.build_url(dict_args_in_out=kwargs))

    @filter_kwargs
    def find(self, **kwargs):
        """
        ?????
        Find a single item with attributes matching ``**kwargs``.
        """
        url = self.build_url(dict_args_in_out=kwargs)

        rl = self._list(
            '%(url)s%(query)s' % {
                'url': url,
                'query': '?%s' % urllib.urlencode(kwargs) if kwargs else '',
            },
            self.collection_key)
        num = len(rl)

        if num == 0:
            return None
        elif num > 1:
            raise NoUniqueMatch
        else:
            return rl[0]
