

from src.players.base_player import BasePlayer
from src.game_master_events.event_set_map import EventSetMap, event_map


class GameMaster(BasePlayer):

    def __init__(self):
        self.events: EventSetMap = event_map

    def invoke_event(self, event_name: str) -> None:

        if event_name not in self.events.get_event_names():
            raise ValueError(f'Please enter a valid event name. Valid event names: {
                             self.events.get_event_names}')

        self.event_map.get_event(event_name)()  # Call the event function
