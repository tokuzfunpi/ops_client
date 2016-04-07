from ops_client.client.base import BaseClient
from ops_client.project.ceilometer import *

class CeilometerClient(BaseClient):
    def __init__(self, **kwargs):
        BaseClient.__init__(self, **kwargs)
        self.event_types = EventTypeManager(self)
        self.events = EventManager(self)
        self.meters = MeterManager(self)
        self.resources = ResourceManager(self)
        self.samples = SampleManager(self)
        self.statistics = StatisticsManager(self)
        self.trait_descriptions = TraitDescriptionManager(self)
        self.traits = TraitManager(self)
        self.alarms = AlarmManager(self)
        self.query = QueryManager(self)
