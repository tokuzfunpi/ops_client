from ops_client.manager.ceilometer import CeilometerBaseManager

def object_class_str(mgr, value, loaded):
	#TODO : no EventType
    return EventType(mgr, {"event_type": value}, loaded)

class EventTypeManager(CeilometerBaseManager):

    def list(self, **kwargs):
        return self._get('/event_types/', obj_class=object_class_str, **kwargs)