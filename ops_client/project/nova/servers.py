"""
Server interface.
"""

import base64
import six
from ops_client.common import strutils
from ops_client.common import crypto
from ops_client.manager.nova import NovaBaseManager

REBOOT_SOFT, REBOOT_HARD = 'SOFT', 'HARD'

class ServerManager(NovaBaseManager):

    def _parse_block_device_mapping(self, block_device_mapping):
        bdm = []

        for device_name, mapping in six.iteritems(block_device_mapping):
            #
            # The mapping is in the format:
            # <id>:[<type>]:[<size(GB)>]:[<delete_on_terminate>]
            #
            bdm_dict = {'device_name': device_name}

            mapping_parts = mapping.split(':')
            source_id = mapping_parts[0]
            if len(mapping_parts) == 1:
                bdm_dict['volume_id'] = source_id

            elif len(mapping_parts) > 1:
                source_type = mapping_parts[1]
                if source_type.startswith('snap'):
                    bdm_dict['snapshot_id'] = source_id
                else:
                    bdm_dict['volume_id'] = source_id

            if len(mapping_parts) > 2 and mapping_parts[2]:
                bdm_dict['volume_size'] = str(int(mapping_parts[2]))

            if len(mapping_parts) > 3:
                bdm_dict['delete_on_termination'] = mapping_parts[3]

            bdm.append(bdm_dict)
        return bdm

    def _boot(self, resource_url, response_key, name, image_id, flavor_id,
              meta=None, files=None, userdata=None, personality = None,
              reservation_id=None, return_raw=False, min_count=None,
              max_count=None, security_groups=None, key_name=None,
              availability_zone=None, block_device_mapping=None,
              block_device_mapping_v2=None, nics=None, scheduler_hints=None,
              config_drive=None, admin_pass=None, disk_config=None, **kwargs):
        """
        Create (boot) a new server.

        :param name: Something to name the server.
        :param image_id: The :class:`Image` to boot with.
        :param flavor_id: The :class:`Flavor` to boot onto.
        :param meta: A dict of arbitrary key/value metadata to store for this
                     server. A maximum of five entries is allowed, and both
                     keys and values must be 255 characters or less.
        :param files: A dict of files to overwrite on the server upon boot.
                      Keys are file names (i.e. ``/etc/passwd``) and values
                      are the file contents (either as a string or as a
                      file-like object). A maximum of five entries is allowed,
                      and each file must be 10k or less.
        :param reservation_id: a UUID for the set of servers being requested.
        :param return_raw: If True, don't try to coearse the result into
                           a Resource object.
        :param security_groups: list of security group names
        :param key_name: (optional extension) name of keypair to inject into
                         the instance
        :param availability_zone: Name of the availability zone for instance
                                  placement.
        :param block_device_mapping: A dict of block device mappings for this
                                     server.
        :param block_device_mapping_v2: A dict of block device mappings V2 for
                                        this server.
        :param nics:  (optional extension) an ordered list of nics to be
                      added to this server, with information about
                      connected networks, fixed ips, etc.
        :param scheduler_hints: (optional extension) arbitrary key-value pairs
                              specified by the client to help boot an instance.
        :param config_drive: (optional extension) If True, enable config drive
                             on the server.
        :param admin_pass: admin password for the server.
        :param disk_config: (optional extension) control how the disk is
                            partitioned when the server is created.
        """

        body = {"server": {
            "name": name,
            "imageRef": image_id if image_id else '',
            "flavorRef": flavor_id,
        }}
        if userdata:
            if hasattr(userdata, 'read'):
                userdata = userdata.read()

            userdata = strutils.safe_encode(userdata)

            userdata_b64 = base64.b64encode(userdata).decode('utf-8')
            body["server"]["user_data"] = userdata_b64
        if meta:
            body["server"]["metadata"] = meta
        if reservation_id:
            body["server"]["reservation_id"] = reservation_id
        if key_name:
            body["server"]["key_name"] = key_name
        if scheduler_hints:
            body['os:scheduler_hints'] = scheduler_hints
        if config_drive:
            body["server"]["config_drive"] = config_drive
        if admin_pass:
            body["server"]["adminPass"] = admin_pass
        if not min_count:
            min_count = 1
        if not max_count:
            max_count = min_count
        body["server"]["min_count"] = min_count
        body["server"]["max_count"] = max_count

        if security_groups:
            body["server"]["security_groups"] =\
             [{'name': sg} for sg in security_groups]

        if files and not personality :
            personality = body['server']['personality'] = []
            for filepath, file_or_string in sorted(files.items(),
                                                   key=lambda x: x[0]):
                if hasattr(file_or_string, 'read'):
                    data = file_or_string.read()
                else:
                    data = file_or_string

                cont = base64.b64encode(data.encode('utf-8')).decode('utf-8')
                personality.append({
                    'path': filepath,
                    'contents': cont,
                })
        elif personality :
            _personality = []
            for _p in personality :
                cont = base64.b64encode(
                    _p.get('contents').encode('utf-8')).decode('utf-8')
                _personality.append({
                    'path': _p.get('path', ''),
                    'contents': cont,
                })
            body['server']['personality'] = _personality

        if availability_zone:
            body["server"]["availability_zone"] = availability_zone

        if block_device_mapping:
            body['server']['block_device_mapping'] = \
                    self._parse_block_device_mapping(block_device_mapping)
        elif block_device_mapping_v2:
            if image_id:
                bdm_dict = {'uuid': image_id, 'source_type': 'image',
                            'destination_type': 'local', 'boot_index': 0,
                            'delete_on_termination': True}
                block_device_mapping_v2.insert(0, bdm_dict)

            body['server']['block_device_mapping_v2'] = \
                block_device_mapping_v2

        if nics is not None:
            all_net_data = []
            for nic_info in nics:
                net_data = {}
                if nic_info.get('net-id'):
                    net_data['uuid'] = nic_info['net-id']
                if (nic_info.get('v4-fixed-ip') and
                    nic_info.get('v6-fixed-ip')):
                    raise Exception(
                        "Only one of 'v4-fixed-ip' and 'v6-fixed-ip' may be"
                        " provided.")
                elif nic_info.get('v4-fixed-ip'):
                    net_data['fixed_ip'] = nic_info['v4-fixed-ip']
                elif nic_info.get('v6-fixed-ip'):
                    net_data['fixed_ip'] = nic_info['v6-fixed-ip']
                if nic_info.get('port-id'):
                    net_data['port'] = nic_info['port-id']
                all_net_data.append(net_data)
            body['server']['networks'] = all_net_data

        if disk_config is not None:
            body['server']['OS-DCF:diskConfig'] = disk_config

        if response_key :
            return self._post(resource_url, body, response_key, **kwargs)
        else :
            return self._post(resource_url, body, **kwargs)

    def _action(self, action, server_id, info=None, raw_body = None, **kwargs):
        return self.base_action(action, server_id, info=info, 
                                raw_body=raw_body, **kwargs)

    def base_action(self, action, server_id, info=None, raw_body = None, 
                    resource_url="/servers/%s/action", **kwargs):
        """
        Perform a server "action" -- reboot/rebuild/resize/etc.
        """
        if not raw_body :
            body = {action: info}
        else :
            body = raw_body
        
        return self._post(resource_url % server_id, body, **kwargs)

    def base_get(self, server_id, response_key = True, 
                 resource_url='/servers/%s', **kwargs):
        """
        Get a server.

        :param server: ID of the :class:`Server` to get.
        :rtype: :class:`Server`
        """
        if response_key :
            return self._get(resource_url % server_id, "server", **kwargs)
        else :
            return self._get(resource_url % server_id, **kwargs)

    def get(self, server_id, response_key = True, **kwargs):
        return self.base_get(server_id, response_key=response_key, **kwargs)


    def list(self, detailed = True, params = {}, response_key = True, **kwargs):
        return self.base_list(detailed=detailed, params=params, 
                              response_key=response_key, **kwargs)

    def base_list(self, detailed=True, params={}, 
                  response_key=True, resource_url='/servers%s', **kwargs):
        """
        Get a list of servers.

        :param detailed: Whether to return detailed server info (optional).
        :param search_opts: Search options to filter out servers (optional).
        :param marker: Begin returning servers that appear later in the server
                       list than that represented by this server id (optional).
        :param limit: Maximum number of servers to return (optional).

        :rtype: list of :class:`Server`
        """        

        detail = ""
        if detailed:
            detail = "/detail"
    
        if response_key :
            return self._get(resource_url % (detail), "servers", 
                             params = params, **kwargs)
        else :
            return self._get(resource_url % (detail), params = params, **kwargs)

    def add_fixed_ip(self, server_id, network_id, **kwargs):
        """
        Add an IP address on a network.

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param network_id: The ID of the network the IP should be on.
        """
        return self._action('addFixedIp', server_id, {'networkId': network_id})

    def remove_fixed_ip(self, server_id, address, **kwargs):
        """
        Remove an IP address.

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param address: The IP address to remove.
        """
        return self._action('removeFixedIp', server_id, {'address': address})

    def add_floating_ip(self, server_id, address, fixed_address=None, **kwargs):
        """
        Add a floating ip to an instance

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param address: The FloatingIP or string floating address to add.
        :param fixed_address: The FixedIP the floatingIP should be
                              associated with (optional)
        """
        address = address.ip if hasattr(address, 'ip') else address
        if fixed_address:
            if hasattr(fixed_address, 'ip'):
                fixed_address = fixed_address.ip
            return self._action('addFloatingIp', server_id,
                         {'address': address, 'fixed_address': fixed_address})
        else:
            return self._action('addFloatingIp', server_id, {'address': address})

    def remove_floating_ip(self, server_id, address, **kwargs):
        """
        Remove a floating IP address.

        :param server: The :class:`Server` (or its ID) to remove an IP from.
        :param address: The FloatingIP or string floating address to remove.
        """
        address = address.ip if hasattr(address, 'ip') else address
        return self._action('removeFloatingIp', server_id, {'address': address})

    def get_vnc_console(self, server_id, console_type, **kwargs):
        """
        Get a vnc console for an instance

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param console_type: Type of vnc console to get ('novnc' or 'xvpvnc')
        """
        return self._action('os-getVNCConsole', server_id, 
                            {'type': console_type})

    def get_spice_console(self, server_id, console_type, **kwargs):
        """
        Get a spice console for an instance

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param console_type: Type of spice console to get ('spice-html5')
        """
        return self._action('os-getSPICEConsole', server_id,
                            {'type': console_type})

    def get_rdp_console(self, server_id, console_type, **kwargs):
        """
        Get a rdp console for an instance

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param console_type: Type of rdp console to get ('rdp-html5')
        """
        return self._action('os-getRDPConsole', server_id,
                            {'type': console_type})

    def get_password(self, server_id, private_key=None):
        """
        Get password for an instance

        Returns the clear password of an instance if private_key is
        provided, returns the ciphered password otherwise.

        Requires that openssl is installed and in the path

        :param server: The :class:`Server` (or its ID) to add an IP to.
        :param private_key: The private key to decrypt password
                            (optional)
        """
        resp, body = self._get("/servers/%s/os-server-password" % server_id)
        ciphered_pw = body.get('password', '') if body else ''
        if private_key and ciphered_pw:
            try:
                return crypto.decrypt_password(private_key, ciphered_pw)
            except Exception as exc:
                return '%sFailed to decrypt:\n%s' % (exc, ciphered_pw)
        return ciphered_pw

    def clear_password(self, server_id, **kwargs):
        """
        Clear password for an instance

        :param server: The :class:`Server` (or its ID) to add an IP to.
        """
        return self._delete("/servers/%s/os-server-password" % server_id, 
                            **kwargs)

    def stop(self, server_id, **kwargs):
        """
        Stop the server.
        """
        return self._action('os-stop', server_id, None, **kwargs)

    def force_delete(self, server_id, **kwargs):
        """
        Force delete the server.
        """
        return self._action('forceDelete', server_id, None, **kwargs)

    def restore(self, server_id, **kwargs):
        """
        Restore soft-deleted server.
        """
        return self._action('restore', server_id, None, **kwargs)

    def start(self, server_id, **kwargs):
        """
        Start the server.
        """
        return self._action('os-start', server_id, None, **kwargs)

    def pause(self, server_id, **kwargs):
        """
        Pause the server.
        """
        return self._action('pause', server_id, None, **kwargs)

    def unpause(self, server_id, **kwargs):
        """
        Unpause the server.
        """
        return self._action('unpause', server_id, None, **kwargs)

    def lock(self, server_id, **kwargs):
        """
        Lock the server.
        """
        return self._action('lock', server_id, None, **kwargs)

    def unlock(self, server_id, **kwargs):
        """
        Unlock the server.
        """
        return self._action('unlock', server_id, None, **kwargs)

    def suspend(self, server_id, **kwargs):
        """
        Suspend the server. (Can not work now, has QEMU issue.)
        """
        return self._action('suspend', server_id, None, **kwargs)

    def resume(self, server_id, **kwargs):
        """
        Resume the server.
        """
        return self._action('resume', server_id, None, **kwargs)

    def rescue(self, server_id, **kwargs):
        """
        Rescue the server.
        """
        return self._action('rescue', server_id, None, **kwargs)

    def unrescue(self, server_id, **kwargs):
        """
        Unrescue the server.
        """
        return self._action('unrescue', server_id, None, **kwargs)

    def shelve(self, server_id, **kwargs):
        """
        Shelve the server.
        """
        return self._action('shelve', server_id, None, **kwargs)

    def shelve_offload(self, server_id, **kwargs):
        """
        Remove a shelved instance from the compute node.
        """
        return self._action('shelveOffload', server_id, None, **kwargs)

    def unshelve(self, server_id, **kwargs):
        """
        Unshelve the server.
        """
        return self._action('unshelve', server_id, None, **kwargs)

    def diagnostics(self, server_id, **kwargs):
        """Retrieve server diagnostics."""
        return self._get("/servers/%s/diagnostics" % server_id, **kwargs)

    def create(self, name, image_id, flavor_id, meta=None, files=None,
               reservation_id=None, min_count=None, personality = None,
               max_count=None, security_groups=None, userdata=None,
               key_name=None, availability_zone=None,
               block_device_mapping=None, block_device_mapping_v2=None,
               nics=None, scheduler_hints=None, config_drive=None, 
               disk_config=None, response_key = True, **kwargs):
        return self.base_create(name, image_id, flavor_id, 
                    meta = meta,
                    files=files,
                    reservation_id=reservation_id, 
                    min_count=min_count,
                    personality = personality,
                    max_count=max_count, 
                    security_groups=security_groups, 
                    userdata=userdata,
                    key_name=key_name, 
                    availability_zone=availability_zone,
                    block_device_mapping=block_device_mapping,
                    block_device_mapping_v2=block_device_mapping_v2,
                    nics=nics,
                    scheduler_hints=scheduler_hints, 
                    config_drive=config_drive, 
                    disk_config=disk_config, 
                    response_key = response_key,
                    **kwargs)


    def base_create(self, name, image_id, flavor_id, meta=None, files=None,
               reservation_id=None, min_count=None, personality = None,
               max_count=None, security_groups=None, userdata=None,
               key_name=None, availability_zone=None,
               block_device_mapping=None, block_device_mapping_v2=None,
               nics=None, scheduler_hints=None, config_drive=None, 
               disk_config=None, response_key = True, 
               resource_url = '/servers', **kwargs):
        """
        Create (boot) a new server.

        :param name: Something to name the server.
        :param image_id: The :class:`Image` to boot with.
        :param flavor_id: The :class:`Flavor` to boot onto.
        :param meta: A dict of arbitrary key/value metadata to store for this
                     server. A maximum of five entries is allowed, and both
                     keys and values must be 255 characters or less.
        :param files: A dict of files to overrwrite on the server upon boot.
                      Keys are file names (i.e. ``/etc/passwd``) and values
                      are the file contents (either as a string or as a
                      file-like object). A maximum of five entries is allowed,
                      and each file must be 10k or less.
        :param userdata: user data to pass to be exposed by the metadata
                      server this can be a file type object as well or a
                      string.
        :param reservation_id: a UUID for the set of servers being requested.
        :param key_name: (optional extension) name of previously created
                      keypair to inject into the instance.
        :param availability_zone: Name of the availability zone for instance
                                  placement.
        :param block_device_mapping: (optional extension) A dict of block
                      device mappings for this server.
        :param block_device_mapping_v2: (optional extension) A dict of block
                      device mappings for this server.
        :param nics:  (optional extension) an ordered list of nics to be
                      added to this server, with information about
                      connected networks, fixed ips, port etc.
        :param scheduler_hints: (optional extension) arbitrary key-value pairs
                            specified by the client to help boot an instance
        :param config_drive: (optional extension) value for config drive
                            either boolean, or volume-id
        :param disk_config: (optional extension) control how the disk is
                            partitioned when the server is created.  possible
                            values are 'AUTO' or 'MANUAL'.
        """
        if not min_count:
            min_count = 1
        if not max_count:
            max_count = min_count
        if min_count > max_count:
            min_count = max_count

        boot_args = [name, image_id, flavor_id]

        boot_kwargs = dict(
            meta=meta, files=files, userdata=userdata,
            reservation_id=reservation_id, min_count=min_count,
            max_count=max_count, security_groups=security_groups,
            key_name=key_name, availability_zone=availability_zone,
            scheduler_hints=scheduler_hints, config_drive=config_drive,
            disk_config=disk_config, personality = personality, **kwargs)

        if block_device_mapping:
            boot_kwargs['block_device_mapping'] = block_device_mapping
        elif block_device_mapping_v2:
            boot_kwargs['block_device_mapping_v2'] = block_device_mapping_v2
        if nics:
            boot_kwargs['nics'] = nics

        if response_key :
            response_key = "server"
            return self._boot(resource_url, response_key, *boot_args,
                              **boot_kwargs)
        else :
            response_key = None
            return self._boot(resource_url, response_key, *boot_args,
                              **boot_kwargs)

    def update(self, server_id, name = None, response_key = True, 
               raw_body = None, **kwargs):
        return self.base_update(server_id, name=name, response_key=response_key,
                                raw_body=raw_body, **kwargs)

    def base_update(self, server_id, name = None, response_key = True, 
                    raw_body = None, resource_url='/servers/%s', **kwargs):
        """
        Update the name or the password for a server.

        :param server: The :class:`Server` (or its ID) to update.
        :param name: Update the server's name.
        """
        if not raw_body :
            if name is None:
                return

            body = {
                "server": {
                    "name": name,
                }
            }
        else :
            body = raw_body

        if response_key :
            return self._put(resource_url % server_id, body, 
                             "server", **kwargs)
        else :
            return self._put(resource_url % server_id, body, **kwargs)

    def change_password(self, server_id, password, **kwargs):
        """
        Update the password for a server.
        """
        return self._action("changePassword", server_id, 
                            {"adminPass": password}, **kwargs)

    def delete(self, server_id, **kwargs):
        return self.base_delete(server_id, **kwargs) 

    def base_delete(self, server_id, resource_url='/servers/%s', **kwargs):
        """
        Delete (i.e. shut down and delete the image) this server.
        """
        return self._delete(resource_url % server_id, **kwargs)        

    def reboot(self, server_id, reboot_type=REBOOT_SOFT, **kwargs):
        """
        Reboot a server.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param reboot_type: either :data:`REBOOT_SOFT` for a software-level
                reboot, or `REBOOT_HARD` for a virtual power cycle hard reboot.
        """
        return self._action('reboot', server_id, {'type': reboot_type}, 
                            **kwargs)

    def rebuild(self, server_id, image_id, password=None, disk_config=None,
                preserve_ephemeral=False, response_key = True, **kwargs):
        """
        Rebuild -- shut down and then re-image -- a server.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param image: the :class:`Image` (or its ID) to re-image with.
        :param password: string to set as password on the rebuilt server.
        :param disk_config: partitioning mode to use on the rebuilt server.
                            Valid values are 'AUTO' or 'MANUAL'
        :param preserve_ephemeral: If True, request that any ephemeral device
            be preserved when rebuilding the instance. Defaults to False.
        """
        body = {'imageRef': image_id}
        if password is not None:
            body['adminPass'] = password
        if disk_config is not None:
            body['OS-DCF:diskConfig'] = disk_config
        if preserve_ephemeral is not False:
            body['preserve_ephemeral'] = True

        resp, body = self._action('rebuild', server_id, body, **kwargs)
        if response_key :
            return resp, body['server']
        else :
            return resp, body
        

    def migrate(self, server, **kwargs):
        """
        Migrate a server to a new host.

        :param server: The :class:`Server` (or its ID).
        """
        return self._action('migrate', server, **kwargs)

    def resize(self, server_id, flavor_id, disk_config=None, **kwargs):
        """
        Resize a server's resources.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param flavor: the :class:`Flavor` (or its ID) to resize to.
        :param disk_config: partitioning mode to use on the rebuilt server.
                            Valid values are 'AUTO' or 'MANUAL'

        Until a resize event is confirmed with :meth:`confirm_resize`, the old
        server will be kept around and you'll be able to roll back to the old
        flavor quickly with :meth:`revert_resize`. All resizes are
        automatically confirmed after 24 hours.
        """
        info = {'flavorRef': flavor_id}
        if disk_config is not None:
            info['OS-DCF:diskConfig'] = disk_config

        return self._action('resize', server_id, info=info, **kwargs)

    def confirm_resize(self, server_id, **kwargs):
        """
        Confirm that the resize worked, thus removing the original server.

        :param server: The :class:`Server` (or its ID) to share onto.
        """
        return self._action('confirmResize', server_id)

    def revert_resize(self, server_id, **kwargs):
        """
        Revert a previous resize, switching back to the old server.

        :param server: The :class:`Server` (or its ID) to share onto.
        """
        return self._action('revertResize', server_id, **kwargs)

    def create_image(self, server_id, image_name, metadata = None, **kwargs):
        """
        Snapshot a server.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param image_name: Name to give the snapshot image
        :param meta: Metadata to give newly-created image entity
        """
        body = {'name': image_name, 'metadata': metadata or {}}
        return self._action('createImage', server_id, body, **kwargs)
        #location = resp.headers['location']
        #image_uuid = location.split('/')[-1]
        #return image_uuid

    def backup(self, server_id, backup_name, backup_type, rotation, **kwargs):
        """
        Backup a server instance.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param backup_name: Name of the backup image
        :param backup_type: The backup type, like 'daily' or 'weekly'
        :param rotation: Int parameter representing how many backups to
                        keep around.
        """
        body = {'name': backup_name,
                'backup_type': backup_type,
                'rotation': rotation}
        return self._action('createBackup', server_id, body, **kwargs)

    def base_list_meta(self, server_id, response_key = True,
                      resource_url = '/servers/%s/metadata', **kwargs):
        return self._get(resource_url % server_id, **kwargs)

    def list_meta(self, server_id, response_key = True, **kwargs):
        return self.base_list_meta(server_id,
                                  response_key=response_key, **kwargs)

    def base_get_meta(self, server_id, metakey, response_key = True,
                      resource_url = '/servers/%s/metadata/%s', **kwargs):
        return self._get(resource_url % (server_id, metakey), **kwargs)

    def get_meta(self, server_id, metakey, response_key = True, **kwargs):
        return self.base_get_meta(server_id, metakey,
                                  response_key=response_key, **kwargs)

    def set_meta(self, server_id, metadata, response_key = True, **kwargs):
        return self.base_set_meta(server_id, metadata, 
                                  response_key=response_key, **kwargs)

    def base_set_meta(self, server_id, metadata, response_key = True, 
                      resource_url='/servers/%s/metadata', **kwargs):
        """
        Set a servers metadata
        :param server: The :class:`Server` to add metadata to
        :param metadata: A dict of metadata to add to the server
        """
        if type(metadata) is dict:
            body = {'metadata': metadata}
            if response_key :
                return self._post(resource_url % server_id, body, 
                                  "metadata", **kwargs)
            else :
                return self._post(resource_url % server_id, body, 
                                  **kwargs)
        else:
            raise TypeError('Metadata Type should be a dict.')

    def base_set_meta_item(self, server_id, key, value,
                           resource_url = '/servers/%s/metadata/%s', **kwargs):
        """
        Updates an item of server metadata
        :param server: The :class:`Server` to add metadata to
        :param key: metadata key to update
        :param value: string value
        """
        body = {'meta': {key: value}}
        return self._put(resource_url % (server_id, key), body, **kwargs)

    def set_meta_item(self, server_id, key, value, **kwargs):
        """
        Updates an item of server metadata
        :param server: The :class:`Server` to add metadata to
        :param key: metadata key to update
        :param value: string value
        """
        return self.base_set_meta_item(server_id, key, value, **kwargs)

    def base_update_meta(self, server_id, metadata, response_key = True, 
                         resource_url = '/servers/%s/metadata', **kwargs):
        if type(metadata) is dict:
            body = {'metadata': metadata}
            if response_key :
                return self._put(resource_url % server_id, body, 
                                  "metadata", **kwargs)
            else :
                return self._put(resource_url % server_id, body, 
                                  **kwargs)
        else:
            raise TypeError('Metadata Type should be a dict.')

    def update_meta(self, server_id, metadata, response_key = True, **kwargs):
        return self.base_update_meta(server_id, metadata,
                                     response_key = response_key, **kwargs)


    def get_console_output(self, server_id, length=None, **kwargs):
        """
        Get text console log output from Server.

        :param server: The :class:`Server` (or its ID) whose console output
                        you would like to retrieve.
        :param length: The number of tail loglines you would like to retrieve.
        """
        return self._action('os-getConsoleOutput',
                            server_id,
                            {'length': length}, **kwargs)

    def base_delete_meta(self, server_id, key,
                         resource_url = '/servers/%s/metadata/%s', **kwargs):
        """
        Delete metadata from an server
        :param server: The :class:`Server` to add metadata to
        :param keys: A list of metadata keys to delete from the server
        """
        return self._delete(resource_url % (server_id, key), **kwargs)

    def delete_meta(self, server_id, key, **kwargs):
        return self.base_delete_meta(server_id, key, **kwargs)

    def live_migrate(self, server_id, host, block_migration, disk_over_commit,
                     **kwargs):
        """
        Migrates a running instance to a new machine.

        :param server: instance id which comes from nova list.
        :param host: destination host name.
        :param block_migration: if True, do block_migration.
        :param disk_over_commit: if True, Allow overcommit.

        """
        return self._action('os-migrateLive', server_id,
                            {'host': host,
                            'block_migration': block_migration,
                            'disk_over_commit': disk_over_commit}, **kwargs)

    def reset_state(self, server_id, state='error', **kwargs):
        """
        Reset the state of an instance to active or error.

        :param server: ID of the instance to reset the state of.
        :param state: Desired state; either 'active' or 'error'.
                      Defaults to 'error'.
        """
        return self._action('os-resetState', server_id, dict(state=state), 
                            **kwargs)

    def reset_network(self, server_id, **kwargs):
        """
        Reset network of an instance.
        """
        return self._action('resetNetwork', server_id, **kwargs)

    def add_security_group(self, server_id, sg_name, **kwargs):
        """
        Add a Security Group to an instance

        :param server: ID of the instance.
        :param security_group: The name of security group to add.

        """
        return self._action('addSecurityGroup', server_id, 
                            {'name': sg_name}, **kwargs)

    def remove_security_group(self, server_id, sg_name, **kwargs):
        """
        Add a Security Group to an instance

        :param server: ID of the instance.
        :param security_group: The name of security group to remove.

        """
        return self._action('removeSecurityGroup', server_id, 
                            {'name': sg_name}, **kwargs)

    def list_security_group(self, server_id, response_key = True, **kwargs):
        """
        List Security Group(s) of an instance

        :param server: ID of the instance.

        """
        if response_key :
            return self._get("/servers/%s/os-security-groups" % server_id,
                              'security_groups', **kwargs)
        else :
            return self._get("/servers/%s/os-security-groups" % server_id,
                              **kwargs)

    def evacuate(self, server_id, host, on_shared_storage, password = None,
                 **kwargs):
        """
        Evacuate a server instance.

        :param server: The :class:`Server` (or its ID) to share onto.
        :param host: Name of the target host.
        :param on_shared_storage: Specifies whether instance files located
                        on shared storage
        :param password: string to set as password on the evacuated server.
        """
        body = {
                'host': host,
                'onSharedStorage': on_shared_storage,
                }

        if password is not None:
            body['adminPass'] = password

        return self._action('evacuate', server_id, body, **kwargs)

    def interface_list(self, server_id, response_key = True, **kwargs):
        """
        List attached network interfaces

        :param server: The :class:`Server` (or its ID) to query.
        """
        if response_key :
            return self._get("/servers/%s/os-interface" % server_id,
                             'interfaceAttachments', **kwargs)
        else :
            return self._get("/servers/%s/os-interface" % server_id,
                             **kwargs)

    def interface_attach(self, server_id, port_id, net_id, fixed_ip,
                         response_key = True, **kwargs):
        """
        Attach a network_interface to an instance.

        :param server: The :class:`Server` (or its ID) to attach to.
        :param port_id: The port to attach.
        """
        body = {'interfaceAttachment': {}}
        if port_id:
            body['interfaceAttachment']['port_id'] = port_id
        if net_id:
            body['interfaceAttachment']['net_id'] = net_id
        if fixed_ip:
            body['interfaceAttachment']['fixed_ips'] = [
                {'ip_address': fixed_ip}]
        if response_key :
            return self._post("/servers/%s/os-interface" % server_id, 
                              body, 'interfaceAttachment', **kwargs)
        else :
            return self._post("/servers/%s/os-interface" % server_id, 
                              body, **kwargs)
        

    def interface_detach(self, server_id, port_id, **kwargs):
        """
        Detach a network_interface from an instance.

        :param server: The :class:`Server` (or its ID) to detach from.
        :param port_id: The port to detach.
        """
        return self._delete("/servers/%s/os-interface/%s" % 
                            (server_id, port_id), **kwargs)
