"""
Aggregate interface.
"""

from ops_client.manager.nova import NovaBaseManager

class AggregateManager(NovaBaseManager):

    def list(self, response_key = True, **kwargs):
        """Get a list of os-aggregates."""
        if response_key :
            return self._get('/os-aggregates', 'aggregates', **kwargs)
        else :
            return self._get('/os-aggregates', **kwargs)

    def create(self, name, availability_zone, response_key = True, **kwargs):
        """Create a new aggregate.

        :param name: Aggregate Name. (string)
        :param availability_zone: Availability Zone Name. (string)
        """
        body = {'aggregate': {'name': name,
                              'availability_zone': availability_zone}}
        if response_key :
            return self._post('/os-aggregates', body, 'aggregate', **kwargs)
        else :
            return self._post('/os-aggregates', body, **kwargs)

    def get(self, aggregate_id, response_key = True, **kwargs):
        """Get details of the specified aggregate."""
        if response_key :
            return self._get('/os-aggregates/%s' % aggregate_id,
                             "aggregate", **kwargs)
        else :
            return self._get('/os-aggregates/%s' % aggregate_id, **kwargs)

    def get_details(self, aggregate_id, **kwargs):
        """Get details of the specified aggregate."""
        return self.get(aggregate_id, **kwargs)

    def update(self, aggregate_id, values, response_key = True, **kwargs):
        """Update the name and/or availability zone.

        :param aggregate_id: Aggregate ID. (uuid)
        :param values: Update Values. (dict)
        """
        if type(values) is dict:
            body = {'aggregate': values}
            if response_key :
                return self._put("/os-aggregates/%s" % aggregate_id,
                                    body, "aggregate", **kwargs)
            else :
                return self._put("/os-aggregates/%s" % aggregate_id,
                                body, **kwargs)
        else:
            raise TypeError('Value Type should be dict.')

    def add_host(self, aggregate_id, host, response_key = True, **kwargs):
        """Add a host into the Host Aggregate.

        :param aggregate_id: Aggregate ID. (uuid)
        :param host: Host Name. (string)
        """
        body = {'add_host': {'host': host}}
        if response_key :
            return self._post("/os-aggregates/%s/action" % aggregate_id,
                                body, "aggregate", **kwargs)
        else :
            return self._post("/os-aggregates/%s/action" % aggregate_id,
                                body, **kwargs)

    def remove_host(self, aggregate_id, host, response_key = True, **kwargs):
        """Remove a host from the Host Aggregate.

        :param aggregate_id: Aggregate ID. (uuid)
        :param host: Host Name. (string)
        """
        body = {'remove_host': {'host': host}}
        if response_key :
            return self._post("/os-aggregates/%s/action" % aggregate_id,
                                body, "aggregate", **kwargs)
        else :
            return self._post("/os-aggregates/%s/action" % aggregate_id,
                                body, **kwargs)

    def set_metadata(self, aggregate_id, metadata,
                     response_key = True, **kwargs):
        """Set a aggregate metadata, replacing the existing metadata.

        :param aggregate_id: Aggregate ID. (uuid)
        :param metadata: Metadata Value. (dict)
        """
        if type(metadata) is dict:
            body = {'set_metadata': {'metadata': metadata}}
            if response_key :
                return self._post("/os-aggregates/%s/action" % aggregate_id,
                                    body, "aggregate", **kwargs)
            else :
                return self._post("/os-aggregates/%s/action" % aggregate_id,
                                    body, **kwargs)
        else:
            raise TypeError('Metadata Type should be dict.')

    def delete(self, aggregate_id, **kwargs):
        """Delete the specified aggregates.

        :param aggregate_id: Aggregate ID. (uuid)
        """
        return self._delete('/os-aggregates/%s' % aggregate_id, **kwargs)
