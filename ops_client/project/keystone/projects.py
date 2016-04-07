from ops_client.manager.keystone import KeystoneBaseManager

class ProjectManager(KeystoneBaseManager):
    """Represents an Identity project.

    Attributes:
        * id: a uuid that identifies the project
        * name: project name
        * description: project description
        * enabled: boolean to indicate if project is enabled

    """
    collection_key = 'projects'
    key = 'project'

    def create_project(self, name, domain_id,
                       description = None, enabled = True):
        return self.create(
            domain_id = domain_id,
            name = name,
            description = description,
            enabled = enabled)

    def list_project(self, domain_id = None, user_id = None, **kwargs):
        """List projects.

        If domain or user are provided, then filter projects with
        those attributes.

        If ``**kwargs`` are provided, then filter projects with
        attributes matching ``**kwargs``.
        """
        base_url = '/users/%s' % user_id if user_id else None
        return self.list(
            base_url = base_url,
            domain_id = domain_id,
            **kwargs)

    def get_project(self, project_id):
        return self.get(project_id = project_id)

    def update_project(self, project_id, name = None, domain_id = None, 
               description = None, enabled=None):
        return self.update(
            project_id = project_id,
            domain_id = domain_id,
            name = name,
            description = description,
            enabled = enabled)

    def delete_project(self, project_id):
        return self.delete(project_id = project_id)
