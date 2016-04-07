from ops_client.common.request import do_request
import json
import os

def get_token(url = 'http://127.0.0.1:35357', 
              user_name = None, 
              user_id = None,
              user_pwd = None, 
              user_domain = None,
              user_domain_id = None,
              project_name = None,
              project_id = None,
              project_domain = None,
              project_domain_id = None,
              version = 'v3'):
    url = os.path.join(url, version, 'auth/tokens')
    _user_info = {
        "domain" : {}
    }
    _project_info = {
        "domain" : {}
    }
    if user_pwd :
        _user_info['password'] = user_pwd
    if user_name :
        _user_info['name'] = user_name
    if user_id :
        _user_info['id'] = user_id
    if user_domain :
        _user_info['domain']['name'] = user_domain
    if user_domain_id :
        _user_info['domain']['id'] = user_domain_id
    if project_name :
        _project_info['name'] = project_name
    if project_id :
        _project_info['id'] = project_id
    if project_domain :
        _project_info['domain']['name'] = project_domain
    if project_domain_id :
        _project_info['domain']['id'] = project_domain_id
    auth_body = {
        "auth" : {
            "identity" : {
                "methods" : ["password"],
                "password" : {
                    "user" : _user_info
                }
            },
            "scope" : {
                "project" : _project_info
            }
        }
    }
    headers = {'Content-Type' : 'application/json'}
    resp, body =  do_request(url, 
                             method = 'POST', 
                             headers = headers,
                             contents = json.dumps(auth_body))

    return resp.headers.get('x-subject-token'), body
        

