from ops_client.manager.sahara import SaharaBaseManager


class JobExecutionManager(SaharaBaseManager):

    def list(self, search_opts=None, **kwargs):
        query_string = self._parse_query_string(search_opts)
        url = '/job-executions%s' % query_string
        return self._get(url, **kwargs)

    def get(self, obj_id, **kwargs):
        url = '/job-executions/%s' % obj_id
        return self._get(url, **kwargs)

    def delete(self, obj_id, **kwargs):
        url = '/job-executions/%s' % obj_id
        return self._delete(url, **kwargs)

    def create(self, job_id, cluster_id, configs, input_id=None,
               output_id=None, interface=None, is_public=None,
               is_protected=None, **kwargs):

        url = "/jobs/%s/execute" % job_id
        data = {
            "cluster_id": cluster_id,
            "job_configs": configs,
        }

        if interface:
            data['interface'] = interface

        # Leave these out if they are null.  For Java job types they
        # are not part of the schema
        io_ids = (("input_id", input_id),
                  ("output_id", output_id))
        for key, value in io_ids:
            if value is not None:
                data.update({key: value})

        self._copy_if_defined(data, is_public=is_public,
                              is_protected=is_protected)

        return self._post(url, data, **kwargs)

    def update(self, obj_id, is_public=None, is_protected=None, **kwargs):

        data = {}
        self._copy_if_defined(data, is_public=is_public,
                              is_protected=is_protected)
        url = '/job-executions/%s' % obj_id
        return self._patch(url, data, **kwargs)

    def cancel(self, obj_id, **kwargs):
        url = '/job-executions/%s/cancel' % obj_id
        return self._get(url, **kwargs)

    def refresh_status(self, obj_id, **kwargs):
        url = '/job-executions/%s/refresh-status' % obj_id
        return self._get(url, **kwargs)
