from ops_client.manager.base import BaseManager


class ManilaBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'manila_url'
