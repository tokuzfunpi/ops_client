from ops_client.client.base import BaseClient
from ops_client.project.keystone import *

class KeystoneClient(BaseClient):

    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)

        self.credentials = CredentialManager(self)
        self.domains = DomainManager(self)
        self.endpoints = EndpointManager(self)
        self.groups = GroupManager(self)
        self.policies = PolicyManager(self)
        self.projects = ProjectManager(self)
        self.roles = RoleManager(self)
        self.services = ServiceManager(self)
        self.users =  UserManager(self)
