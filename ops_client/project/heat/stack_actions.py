from ops_client.manager.heat import HeatBaseManager

class StackActionManager(HeatBaseManager):
    def suspend(self, stack_name, stack_id, **kwargs):
        """Suspend a stack."""
        body = {'suspend': None}
        url = '/stacks/%s/%s/actions' % (stack_name, stack_id)
        return self._post(url, body, **kwargs)

    def resume(self, stack_name, stack_id, **kwargs):
        """Resume a stack."""
        body = {'resume': None}
        url = '/stacks/%s/%s/actions' % (stack_name, stack_id)
        return self._post(url, body, **kwargs)

    def cancel_update(self, stack_name, stack_id, **kwargs):
        """Cancel running update of a stack."""
        body = {'cancel_update': None}
        url = '/stacks/%s/%s/actions' % (stack_name, stack_id)
        return self._post(url, body, **kwargs)

    def check(self, stack_name, stack_id, **kwargs):
        """Check a stack."""
        body = {'check': None}
        url = '/stacks/%s/%s/actions' % (stack_name, stack_id)
        return self._post(url, body, **kwargs)

    def _action(self, stack_name, stack_id, action, 
                info=None, raw_body=None, **kwargs):
        if not raw_body:
            body = {action: info}
        else:
            body = raw_body
        url = '/stacks/%s/%s/actions' % (stack_name, stack_id)
        return self._post(url, body, **kwargs)