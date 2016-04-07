from ops_client.manager.cinder import CinderBaseManager

class AvailabilityZoneManager(CinderBaseManager):
    def list(self, detailed=False, **kwargs):
        """Lists all availability zones.

        :rtype: list of :class:`AvailabilityZone`
        """
        if detailed is True:
            return self._get("/os-availability-zone/detail", **kwargs)
        else:
            return self._get("/os-availability-zone", **kwargs)
