from ops_client.common.auth import get_token

class AuthClient():

    def __init__(self, keystone_url):
        self.keystone_url = keystone_url

    def authenticate(self,
                     user_name = None, 
                     user_id = None,
                     user_pwd = None, 
                     user_domain = None,
                     user_domain_id = None,
                     project_name = None,
                     project_id = None,
                     project_domain = None,
                     project_domain_id = None):
        token, resp_body = \
            get_token(url = self.keystone_url, 
                      user_name = user_name, 
                      user_id = user_id,
                      user_pwd = user_pwd, 
                      user_domain = user_domain,
                      user_domain_id = user_domain_id,
                      project_name = project_name,
                      project_id = project_id,
                      project_domain = project_domain,
                      project_domain_id = project_domain_id,
                      version = 'v3')     
        #TBD
        token_body = resp_body['token']
        return token, token_body
