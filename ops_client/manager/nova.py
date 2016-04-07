from ops_client.manager.base import BaseManager

class NovaBaseManager(BaseManager):

    def __init__(self, api):
        self.api = api
        self.url_type = 'nova_url'
            
