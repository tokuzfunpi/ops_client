from ops_client.manager.base import BaseManager

class CinderBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'cinder_url'
