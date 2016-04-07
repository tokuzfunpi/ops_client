from ops_client.manager.ceilometer import CeilometerBaseManager
import six

class StatisticsManager(CeilometerBaseManager):

    def _build_aggregates(self, aggregates):
        url_aggregates = []
        for aggregate in aggregates:
            if 'param' in aggregate:
                url_aggregates.insert(
                    0,
                    "aggregate.param=%(param)s" % aggregate
                )
                url_aggregates.insert(
                    0,
                    "aggregate.func=%(func)s" % aggregate
                )
            else:
                url_aggregates.append(
                    "aggregate.func=%(func)s" % aggregate
                )
        return url_aggregates

    def list(self, meter_name, q=None, period=None,
             groupby=[], aggregates=[], **kwargs):
        p = ['period=%s' % period] if period else []
        if isinstance(groupby, six.string_types):
            groupby = [groupby]
        p.extend(['groupby=%s' % g for g in groupby] if groupby else [])
        p.extend(self._build_aggregates(aggregates))
        path = self.build_url('/meters/' + meter_name + '/statistics', q, p)
        return self._get(path, **kwargs)