from ops_client.manager.neutron import NeutronBaseManager

class MeteringLabelManager(NeutronBaseManager):

    def create_metering_label(self, metering_label_body = None, **kwargs):
        """Creates a metering label.

        :param kwargs: metering label values.
        """
        _body = {}
        if metering_label_body and type(metering_label_body) == dict :
            _body.update(metering_label_body)
        body = {"metering_label":_body}
        return self._post(self.metering_labels_path, body=body)

    def delete_metering_label(self, label):
        """Deletes the specified metering label.

        :param label: ID of the label.
        """
        return self._delete(self.metering_label_path % (label))

    def list_metering_labels(self, params = None):
        """Fetches a list of all metering labels for a tenant."""
        return self._get(self.metering_labels_path, params=params)

    def show_metering_label(self, metering_label, params = None):
        """Fetches information of a certain metering label.

        :param metering_label: ID of the metering label.
        """
        return self._get(self.metering_label_path %
                        (metering_label), params=params)

    def create_metering_label_rule(self, metering_label_id, direction,
                                   remote_ip_prefix, metering_label_body = None,
                                   **kwargs):
        """Creates a metering label rule.

        :param metering_label_id: ID of the metering label.
        :param direction: 'ingress' or 'engress'.
        :param remote_ip_prefix: IP prefix.
        """
        _body = {
            "metering_label_id":metering_label_id,
            "direction":direction,
            "remote_ip_prefix":remote_ip_prefix        
        }
        if metering_label_body and type(metering_label_body) == dict :
            _body.update(metering_label_body)
        body = {"metering_label_rule":_body}
        return self._post(self.metering_label_rules_path, body=body)

    def delete_metering_label_rule(self, rule):
        """Deletes the specified metering label rule.

        :param rule: ID of the metering label rule.
        """
        return self._delete(self.metering_label_rule_path % (rule))

    def list_metering_label_rules(self, params = None):
        """Fetches a list of all metering label rules for a label."""
        return self._get(self.metering_label_rules_path, params=params)

    def show_metering_label_rule(self, metering_label_rule, params = None):
        """Fetches information of a certain metering label rule.

        :param metering_label_id: ID of the metering label rule.
        """
        return self._get(self.metering_label_rule_path %
                        (metering_label_rule), params=params)
