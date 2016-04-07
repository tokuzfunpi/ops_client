from ops_client.manager.base import BaseManager

class LBaaSBaseManager(BaseManager):

    vips_path = "/vips"
    vip_path = "/vips/%(vip)s"
    pools_path = "/pools"
    pool_path = "/pools/%(pool)s"
    pool_path_stats = "/pools/%(pool)s/stats"
    members_path = "/members"
    member_path = "/members/%(member)s"
    health_monitors_path = "/health_monitors"
    health_monitor_path = "/health_monitors/%(health_monitor)s"
    associate_pool_health_monitors_path = "/pools/%(pool)s/health_monitors"
    disassociate_pool_health_monitors_path = (
        "/pools/%(pool)s/health_monitors/%(health_monitor)s")

    LOADBALANCER_POOLS = '/loadbalancer-pools'
    LOADBALANCER_AGENT = '/loadbalancer-agent'

    agent_path = "/agents/%(agent)s"

    # API has no way to report plurals, so we have to hard code them
    EXTED_PLURALS = {'vips': 'vip',
                     'pools': 'pool',
                     'members': 'member',
                     'health_monitors': 'health_monitor',
                     }
    # 8192 Is the default max URI len for eventlet.wsgi.server
    MAX_URI_LEN = 8192

    def __init__(self, api):
        self.api = api
        self.url_type = 'neutron_url'

    def base_list(self, obj_info = None, params = None,
                  resource_url = None, **kwargs):
        return self._get(resource_url, params = params, **kwargs)

    def base_show(self, obj_info = None, params = None, 
                  resource_url = None, **kwargs):
        return self._get(resource_url % (obj_info), params = params, **kwargs)

    def base_create(self, obj_info = None, body = None,
                    resource_url = None, **kwargs):
        if obj_info:
            return self._post(resource_url % (obj_info), body = body, **kwargs)
        else:
            return self._post(resource_url, body = body, **kwargs)

    def base_update(self, obj_info = None, body = None,
                    resource_url = None, **kwargs):
        return self._put(resource_url % (obj_info), body = body, **kwargs)

    def base_delete(self, obj_info = None,
                    resource_url = None, **kwargs):
        return self._delete(resource_url % (obj_info), **kwargs)
