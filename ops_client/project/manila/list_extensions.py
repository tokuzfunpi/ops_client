from ops_client.manager.manila import ManilaBaseManager


class ListExtManager(ManilaBaseManager):

    def show_all(self, **kwargs):
        return self._get("/extensions", **kwargs)
