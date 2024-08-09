from src.game_master_events.events import event1, event2, event3

class EventSetMap():

    def __init__(self, events: dict[str, function]):
        
        self.events: dict[str, function] = events

    def get_event(self, name: str) -> function: return self.events[name]

    def get_events(self) -> set:
        return {event for _, event in self.events.items()}

    def get_event_names(self) -> set:
        return {event_name for _, event_name in self.events.items()}

    
event_map = EventSetMap({
    'event1': event1,
    'event2': event2
    })