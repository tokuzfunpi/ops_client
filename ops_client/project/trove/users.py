from ops_client.manager.trove import TroveBaseManager
from six.moves.urllib import parse

class UserManager(TroveBaseManager):
    def quote_user_host(self, user, host):
        quoted = ''
        if host:
            quoted = parse.quote("%s@%s" % (user, host))
        else:
            quoted = parse.quote("%s" % user)
        return quoted.replace('.', '%2e')

    def create(self, instance, users, **kwargs):
        """Create users with permissions to the specified databases."""
        body = {"users": users}
        return self._post("/instances/%s/users" % instance, body, **kwargs)

    def delete(self, instance, username, hostname = None, **kwargs):
        """Delete an existing user in the specified instance."""
        user = self.quote_user_host(username, hostname)
        return self._delete("/instances/%s/users/%s" % (instance, user),
                            **kwargs)

    def list(self, instance, limit = None, marker = None,
             response_key = True, **kwargs):
        """Get a list of all Users from the instance's Database.

        :rtype: list of :class:`User`.
        """
        url = self.build_url("/instances/%s/users" % instance,
                             limit = limit,
                             marker = marker)
        if response_key :
            return self._get(url, "users", **kwargs)
        else :
            return self._get(url, **kwargs)

    def get(self, instance, username, hostname = None,
            response_key = True, **kwargs):
        """Get a single User from the instance's Database.

        :rtype: :class:`User`.
        """
        user = self.quote_user_host(username, hostname)
        if response_key :
            return self._get("/instances/%s/users/%s" % (instance, user),
                             "user", **kwargs)
        else :
            return self._get("/instances/%s/users/%s" % (instance, user),
                             **kwargs)

    def update_attributes(self, instance, username, newuserattr = None,
                          hostname = None, **kwargs):
        """Update attributes of a single User in an instance.

        :rtype: :class:`User`.
        """
        if not newuserattr:
            raise Exception("No updates specified for user %s" % username)
        user = self.quote_user_host(username, hostname)
        user_dict = {}
        user_dict['user'] = newuserattr
        return self._put("/instances/%s/users/%s" % (instance, user),
                             user_dict, **kwargs)

    def list_access(self, instance, username, hostname = None,
                    response_key = True, **kwargs):
        """Show all databases the given user has access to."""
        user = self.quote_user_host(username, hostname)
        if response_key :
            return self._get("/instances/%s/users/%s/databases" %
                             (instance, user), "databases", **kwargs)
        else :
            return self._get("/instances/%s/users/%s/databases" %
                             (instance, user), **kwargs)

    def grant(self, instance, username, databases, hostname = None, **kwargs):
        """Allow an existing user permissions to access a database."""
        user = self.quote_user_host(username, hostname)
        dbs = {'databases': [{'name': db} for db in databases]}

        return self._put("/instances/%s/users/%s/databases" %
                         (instance, user), dbs, **kwargs)

    def revoke(self, instance, username, database, hostname = None, **kwargs):
        """Revoke from an existing user access permissions to a database."""
        user = self.quote_user_host(username, hostname)
        return self._delete("/instances/%s/users/%s/databases/%s" %
                            (instance, user, database), **kwargs)

    def change_passwords(self, instance, users, **kwargs):
        """Change the password for one or more users."""
        user_dict = {"users": users}
        return self._put("/instances/%s/users" % instance, user_dict, **kwargs)