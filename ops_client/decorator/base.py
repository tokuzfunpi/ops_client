from ops_client.common.exception import UnAuthorizedError

def check_token(func):
    def wrapper(self, *args, **kwargs):
        if self.api.token == None :
            raise UnAuthorizedError()
        return func(self, *args, **kwargs)
    return wrapper

def check_target_url(func):
    def wrapper(self, *args, **kwargs):
        url_type = self.url_type
        if not hasattr(self.api, url_type):
            raise AttributeError(url_type)
        return func(self, *args, **kwargs)
    return wrapper
