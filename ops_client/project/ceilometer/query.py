from ops_client.manager.ceilometer import CeilometerBaseManager

query_type = ['alarms', 'alarms_history', 'samples']

class QueryManager(CeilometerBaseManager):

    def query(self, qtype, filter=None, orderby=None, limit=None, **kwargs):
        if qtype in query_type:
            self.path_suffix = "/"+"/".join(qtype.split("_"))
        else:
            raise Exception(
                "Query Type Must be alarms, alarms_history or samples")
        query = {}
        if filter:
            query["filter"] = filter
        if orderby:
            query["orderby"] = orderby
        if limit:
            query["limit"] = limit

        url = '/query%s' % self.path_suffix
        return self._post(url, body=query, **kwargs)