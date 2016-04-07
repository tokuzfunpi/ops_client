"""
Security group rules interface.
"""

from ops_client.manager.nova import NovaBaseManager
from ops_client.common import exception

class SecurityGroupRuleManager(NovaBaseManager):
    
    def create(self, parent_group_id, ip_protocol=None, from_port=None,
               to_port=None, cidr=None, group_id=None,
               response_key = True, **kwargs):
        """
        Create a security group rule

        :param ip_protocol: IP protocol, one of 'tcp', 'udp' or 'icmp'
        :param from_port: Source port
        :param to_port: Destination port
        :param cidr: Destination IP address(es) in CIDR notation
        :param group_id: Security group id (int)
        :param parent_group_id: Parent security group id (int)
        """
        try:
            from_port = int(from_port)
        except (TypeError, ValueError):
            raise exception.CommandError("From port must be an integer.")
        try:
            to_port = int(to_port)
        except (TypeError, ValueError):
            raise exception.CommandError("To port must be an integer.")
        if ip_protocol.upper() not in ['TCP', 'UDP', 'ICMP']:
            raise exception.CommandError("Ip protocol must be 'tcp', 'udp'"
                                            ", or 'icmp'.")

        body = {"security_group_rule": {
                    "ip_protocol": ip_protocol,
                    "from_port": from_port,
                    "to_port": to_port,
                    "cidr": cidr,
                    "group_id": group_id,
                    "parent_group_id": parent_group_id}}

        if response_key :
            return self._post('/os-security-group-rules', body,
                                'security_group_rule', **kwargs)
        else :
            return self._post('/os-security-group-rules', body, **kwargs)

    def delete(self, rule_id):
        """
        Delete a security group rule

        :param rule: The security group rule to delete (ID or Class)
        """
        return self._delete('/os-security-group-rules/%s' % rule_id)