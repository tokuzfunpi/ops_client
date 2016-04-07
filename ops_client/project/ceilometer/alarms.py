from ops_client.manager.ceilometer import CeilometerBaseManager
from ops_client.common.exception import NotFound
from ops_client.project.ceilometer import utils
import six
import json

UPDATABLE_ATTRIBUTES = [
    'name',
    'description',
    'type',
    'state',
    'enabled',
    'alarm_actions',
    'ok_actions',
    'insufficient_data_actions',
    'repeat_actions',
    'threshold_rule',
    'combination_rule',
]
CREATION_ATTRIBUTES = UPDATABLE_ATTRIBUTES + ['project_id', 'user_id',
                                              'time_constraints']

class AlarmManager(CeilometerBaseManager):

    @staticmethod
    def _path(id=None):
        return '/alarms/%s' % id if id else '/alarms'

    def list(self, q=None, **kwargs):
        path = self.build_url(self._path(), q)
        return self._get(path, **kwargs)

    def get(self, alarm_id, **kwargs):
        try:
            return self._get(self._path(alarm_id), expect_single=True, 
                             **kwargs)
        except IndexError:
            return None
        except NotFound():
            # When we try to get deleted alarm HTTPNotFound occurs
            # or when alarm doesn't exists this exception don't must
            # go deeper because cleanUp() (method which remove all
            # created things like instance, alarm, etc.) at scenario
            # tests doesn't know how to process it
            return None

    @classmethod
    def _compat_legacy_alarm_kwargs(cls, kwargs, create=False):
        cls._compat_counter_rename_kwargs(kwargs, create)
        cls._compat_alarm_before_rule_type_kwargs(kwargs, create)

    @staticmethod
    def _compat_counter_rename_kwargs(kwargs, create=False):
        # NOTE(jd) Compatibility with Havana-2 API
        if 'counter_name' in kwargs:
            warnings.warn("counter_name has been renamed to meter_name",
                          DeprecationWarning)
            kwargs['meter_name'] = kwargs['counter_name']

    @staticmethod
    def _compat_alarm_before_rule_type_kwargs(kwargs, create=False):
        # NOTE(sileht) Compatibility with Havana-3 API
        if create and 'type' not in kwargs:
            warnings.warn("alarm without type set is deprecated",
                          DeprecationWarning)
            kwargs['type'] = 'threshold'

        for field in ['period', 'evaluation_periods', 'threshold',
                      'statistic', 'comparison_operator', 'meter_name']:
            if field in kwargs:
                kwargs.setdefault('threshold_rule', {})[field] = kwargs[field]
                del kwargs[field]

        if 'matching_metadata' in kwargs:
            query = []
            for key in kwargs['matching_metadata']:
                query.append({'field': key,
                              'op': 'eq',
                              'value': kwargs['matching_metadata'][key]})
            del kwargs['matching_metadata']
            kwargs['threshold_rule']['query'] = query

    @staticmethod
    def _merge_time_constraints(existing_tcs, kwargs):
        new_tcs = kwargs.get('time_constraints', [])
        if not existing_tcs:
            updated_tcs = new_tcs
        else:
            updated_tcs = [dict(tc) for tc in existing_tcs]
            for tc in new_tcs:
                for i, old_tc in enumerate(updated_tcs):
                    if old_tc['name'] == tc['name']:  # if names match, merge
                        utils.merge_nested_dict(updated_tcs[i], tc)
                        break
                else:
                    updated_tcs.append(tc)
        tcs_to_remove = kwargs.get('remove_time_constraints', [])
        for tc in updated_tcs:
            if tc['name'] in tcs_to_remove:
                updated_tcs.remove(tc)
        return updated_tcs

    def create(self, body, **kwargs):
        self._compat_legacy_alarm_kwargs(body, create=True)
        body = dict((key, value) for (key, value) in body.items()
                   if key in CREATION_ATTRIBUTES)
        return self._post(self._path(), body, **kwargs)

    def update(self, alarm_id, update_body, **kwargs):
        self._compat_legacy_alarm_kwargs(update_body)
        updated = self.get(alarm_id)[1]
        updated['time_constraints'] = self._merge_time_constraints(
            updated.get('time_constraints', []), update_body)
        update_body = dict((k, v) for k, v in update_body.items()
                      if k in updated and k in UPDATABLE_ATTRIBUTES)
        utils.merge_nested_dict(updated, update_body, depth=1)
        return self._put(self._path(alarm_id), updated, **kwargs)

    def delete(self, alarm_id, **kwargs):
        return self._delete(self._path(alarm_id), **kwargs)

    def set_state(self, alarm_id, state, **kwargs):
        return self._put('%s/state' % self._path(alarm_id),
                         json.dumps(state), **kwargs)

    def get_state(self, alarm_id, **kwargs):
        return self._get('%s/state' % self._path(alarm_id), **kwargs)

    def get_history(self, alarm_id, q=None, **kwargs):
        path = '%s/history' % self._path(alarm_id)
        url = self.build_url(path, q)
        return self._get(url, **kwargs)
