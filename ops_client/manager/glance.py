from ops_client.manager.base import BaseManager

class GlanceBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'glance_url'
