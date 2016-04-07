from ops_client.client.base import BaseClient
from ops_client.project.glance import *

class GlanceClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.images = ImageManager(self)
        self.image_members = ImageMemberManager(self)
        self.image_tags = ImageTagManager(self)
        self.schema = SchemaManager(self)
        self.metadef_ns = MetaDefNamespaceManager(self)
        self.metadef_rt = MetaDefResourceTypeManager(self)
        self.metadef_prop = MetaDefPropertyManager(self)
        self.metadef_obj = MetaDefObjectManager(self)
