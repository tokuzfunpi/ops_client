from ops_client.manager.manila import ManilaBaseManager


class AvailabilityZoneManager(ManilaBaseManager):

    def get(self, **kwargs):
        return self._get("/os-availability-zone", **kwargs)
