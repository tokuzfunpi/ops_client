"""
Availability Zone interface.
"""

from ops_client.manager.nova import NovaBaseManager

class AvailabilityZoneManager(NovaBaseManager):

    def list(self, detailed=True, response_key = True, **kwargs):
        """
        Get a list of all availability zones.

        :rtype: list of :class:`AvailabilityZone`
        """
        if detailed is True:
            if response_key :
                return self._get("/os-availability-zone/detail",
                                  "availabilityZoneInfo", **kwargs)
            else :
                return self._get("/os-availability-zone/detail", **kwargs)
        else:
            if response_key :
                return self._get("/os-availability-zone",
                                  "availabilityZoneInfo", **kwargs)
            else :
                return self._get("/os-availability-zone", **kwargs)
