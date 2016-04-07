"""
Flavor interface.
"""
from ops_client.common import strutils
from ops_client.common import exception
from ops_client.manager.nova import NovaBaseManager

class FlavorManager(NovaBaseManager):

    def _build_body(self, name, ram, vcpus, disk, id, swap,
                    ephemeral, rxtx_factor, is_public):
        return {
            "flavor": {
                "name": name,
                "ram": ram,
                "vcpus": vcpus,
                "disk": disk,
                "id": id,
                "swap": swap,
                "OS-FLV-EXT-DATA:ephemeral": ephemeral,
                "rxtx_factor": rxtx_factor,
                "os-flavor-access:is_public": is_public,
            }
        }

    def list(self, detailed=True, params = None, response_key = True, **kwargs):
        """
        Get a list of all flavors.

        :rtype: list of :class:`Flavor`.
        """
        detail = ""
        if detailed:
            detail = "/detail"

        if response_key :
            return self._get("/flavors%s" % (detail), "flavors",
                             params = params, **kwargs)
        else :
            return self._get("/flavors%s" % (detail), params = params, **kwargs)

    def get(self, flavor_id, response_key = True, **kwargs):
        """
        Get a specific flavor.

        :param flavor: The ID of the :class:`Flavor` to get.
        :rtype: :class:`Flavor`
        """
        if response_key :
            return self._get("/flavors/%s" % flavor_id, "flavor", **kwargs)
        else :
            return self._get("/flavors/%s" % flavor_id, **kwargs)

    def delete(self, flavor_id, **kwargs):
        """
        Delete a specific flavor.

        :param flavor: The ID of the :class:`Flavor` to get.
        """
        return self._delete("/flavors/%s" % flavor_id, **kwargs)

    def create(self, name, ram, vcpus, disk, flavorid="auto",
               ephemeral=0, swap=0, rxtx_factor=1.0, is_public=True,
               response_key = True, **kwargs):
        """
        Create a flavor.

        :param name: Descriptive name of the flavor
        :param ram: Memory in MB for the flavor
        :param vcpus: Number of VCPUs for the flavor
        :param disk: Size of local disk in GB
        :param flavorid: ID for the flavor (optional). You can use the reserved
                         value ``"auto"`` to have Nova generate a UUID for the
                         flavor in cases where you cannot simply pass ``None``.
        :param swap: Swap space in MB
        :param rxtx_factor: RX/TX factor
        :rtype: :class:`Flavor`
        """

        try:
            ram = int(ram)
        except (TypeError, ValueError):
            raise exception.CommandError("Ram must be an integer.")
        try:
            vcpus = int(vcpus)
        except (TypeError, ValueError):
            raise exception.CommandError("VCPUs must be an integer.")
        try:
            disk = int(disk)
        except (TypeError, ValueError):
            raise exception.CommandError("Disk must be an integer.")

        if flavorid == "auto":
            flavorid = None

        try:
            swap = int(swap)
        except (TypeError, ValueError):
            raise exception.CommandError("Swap must be an integer.")
        try:
            ephemeral = int(ephemeral)
        except (TypeError, ValueError):
            raise exception.CommandError("Ephemeral must be an integer.")
        try:
            rxtx_factor = float(rxtx_factor)
        except (TypeError, ValueError):
            raise exception.CommandError("rxtx_factor must be a float.")

        try:
            is_public = strutils.bool_from_string(is_public, True)
        except Exception:
            raise exception.CommandError("is_public must be a boolean.")

        body = self._build_body(name, ram, vcpus, disk, flavorid, swap,
                                ephemeral, rxtx_factor, is_public)

        if response_key :
            return self._post("/flavors", body, "flavor", **kwargs)
        else :
            return self._post("/flavors", body, **kwargs)

    def set_keys(self, flavor_id, metadata = {}, response_key = True, **kwargs):
        """
        Set extra specs on a flavor.

        :param metadata: A dict of key/value pairs to be set
        """
        body = {'extra_specs': metadata}

        if response_key :
            return self._post("flavors/%s/os-extra_specs" % flavor_id,
                body, "extra_specs", **kwargs)
        else :
            return self._post("flavors/%s/os-extra_specs" % flavor_id,
                body, **kwargs)

    def unset_keys(self, flavor_id, metakey, **kwargs):
        """
        Unset extra specs on a flavor.

        :param keys: A list of keys to be unset
        """
        return self._delete(
            "/flavors/%s/os-extra_specs/%s" %(flavor_id, metakey), **kwargs)

    def get_keys(self, flavor_id, response_key = True, **kwargs):
        """
        Get extra specs from a flavor.
        """
        if response_key :
            return self._get("flavors/%s/os-extra_specs" % flavor_id,
                             "extra_specs", **kwargs)
        else :
            return self._get("flavors/%s/os-extra_specs" % flavor_id, **kwargs)

    def update_key(self, flavor_id, metakey, update_value, **kwargs):
        """
        Update extra specs from a flavor.
        """
        body = {metakey: update_value}
        return self._put(
            "flavors/%s/os-extra_specs/%s" %(flavor_id, metakey),
            body, **kwargs)
