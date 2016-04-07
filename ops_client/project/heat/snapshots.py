from ops_client.manager.heat import HeatBaseManager

class SnapshotManager(HeatBaseManager):
    def create(self, stack_name, stack_id, name=None, **kwargs):
        """Snapshot a stack."""
        data = {}
        if name:
            data['name'] = name
        url = '/stacks/%s/%s/snapshots' %(stack_name, stack_id)
        return self._post(url, data, **kwargs)

    def get(self, stack_name, stack_id, snapshot_id,
            response_key=True, **kwargs):
        url = '/stacks/%s/%s/snapshots/%s' %(stack_name, stack_id, snapshot_id)
        if response_key:
            return self._get(url, 'snapshot', **kwargs)
        else:
            return self._get(url, **kwargs)

    def delete(self, stack_name, stack_id, snapshot_id, **kwargs):
        url = '/stacks/%s/%s/snapshots/%s' %(stack_name, stack_id, snapshot_id)
        return self._delete(url, **kwargs)

    def restore(self, stack_name, stack_id, snapshot_id, **kwargs):
        url = '/stacks/%s/%s/snapshots/%s/restore' \
              %(stack_name, stack_id, snapshot_id)
        return self.base_post(url, **kwargs)

    def list(self, stack_name, stack_id, response_key=True, **kwargs):
        url = '/stacks/%s/%s/snapshots' %(stack_name, stack_id)
        if response_key:
            return self._get(url, 'snapshots', **kwargs)
        else:
            return self._get(url, **kwargs)