from ops_client.manager.neutron import NeutronBaseManager

class RouterManager(NeutronBaseManager):

    def list_routers(self, params = None, **kwargs):
        """Fetches a list of all routers for a tenant."""
        # Pass filters in "params" argument to do_request
        return self._get(self.routers_path, params=params, **kwargs)

    def show_router(self, router, params = None, **kwargs):
        """Fetches information of a certain router.

        :param router: ID of the router.
        """
        return self._get(self.router_path % (router), params=params, **kwargs)

    def create_router(self, router_body, **kwargs):
        """Creates a new router.

        :param kwargs: router values.
        """
        body = {
            "router" : router_body
        }
        return self._post(self.routers_path, body=body, **kwargs)

    def update_router(self, router_id, router_body, **kwargs):
        """Updates a router.

        :param router_id: ID of the router.
        """
        body = {
            "router" : router_body
        }
        return self._put(self.router_path % (router_id), body=body, **kwargs)

    def delete_router(self, router_id, **kwargs):
        """Deletes the specified router.

        :param router_id: ID of the router.
        """
        return self._delete(self.router_path % (router_id), **kwargs)

    def add_interface_router(self, router_id, interface, **kwargs):
        """Adds an internal network interface to the specified router.

        :param router_id: ID of the router.
        :param interface: other keyword argument.
        """
        return self._put((self.router_path % router_id) + "/add_router_interface",
                        body = interface, **kwargs)

    def remove_interface_router(self, router_id, interface, **kwargs):
        """Removes an internal network interface from the specified router.

        :param router: ID of the router.
        :param interface: other keyword argument.
        """
        return self._put((self.router_path % router_id) +
                        "/remove_router_interface", body = interface, **kwargs)

    def add_gateway_router(self, router, gw_router, **kwargs):
        """Adds an external network gateway to the specified router.

        :param router: ID of the router.
        :param gw_router: other keyword argument.
        """
        body={'router': {'external_gateway_info': gw_router}}
        print body
        return self._put((self.router_path % router),
                         body=body, **kwargs)

    def remove_gateway_router(self, router_id, **kwargs):
        """Removes an external network gateway from the specified router.

        :param router: ID of the router.
        """
        return self._put((self.router_path % router_id),
                         body={'router': {'external_gateway_info': {}}},
                         **kwargs)
