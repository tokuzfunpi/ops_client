from ops_client.client.base import BaseClient
from ops_client.project.designate import *

class DesignateClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.zones = ZoneManager(self)
        self.recordset = RecordSetManager(self)
        self.tld = TldManager(self)
        self.blacklist = BlackListManager(self)
        self.quota = QuotaManager(self)
        self.pool = PoolManager(self)
        self.nameserver = NameServerManager(self)
        self.dns_limit = LimitManager(self)
        #TODO not workring
        #TODO need region in keystone records
        self.floatingip = FloatingIPManager(self)
        self.dns_tenant = TenantManager(self)
        self.dns_count = CountManager(self)
