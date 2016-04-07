import six
from six.moves.urllib import parse
from ops_client.manager.heat import HeatBaseManager

class EventManager(HeatBaseManager):
    def list(self, stack_name, stack_id, resource_name=None,
             response_key=True, filters={}, **kwargs):
        """Get a list of events.
        :param stack_id: ID of stack the events belong to
        :param resource_name: Optional name of resources to filter events by
        :rtype: list of :class:`Event`
        """
        params = {}
        if filters:
            params.update(filters)

        base_url = '/stacks/%s' % stack_name

        if not resource_name:
            url = base_url + '/%s/events' % stack_id
        else:
            url = base_url + '/%s/resources/%s/events' \
                     %(stack_id, resource_name)

        if params:
            url += '?%s' % parse.urlencode(params, True)

        if response_key:
            return self._get(url, 'events', **kwargs)
        else:
            return self._get(url, **kwargs)

    def get(self, stack_name, stack_id, resource_name, event_id,
            response_key=True, **kwargs):
        """Get the details for a specific event.

        :param stack_id: ID of stack containing the event
        :param resource_name: ID of resource the event belongs to
        :param event_id: ID of event to get the details for
        """
        url = '/stacks/%s/%s/resources/%s/events/%s' \
                 %(stack_name, stack_id, resource_name, event_id)
        if response_key:
            return self._get(url, 'event', **kwargs)
        else:
            return self._get(url, **kwargs)
