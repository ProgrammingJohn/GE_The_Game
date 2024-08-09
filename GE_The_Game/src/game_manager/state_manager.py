from src.players.player import Player
from src.players.game_master import GameMaster
from src.game_manager.game_enviornment_state import GameEnviornmentConditions


class StateManager():

    def __init__(self):

        self.GAME_ENV_VARS = GameEnviornmentConditions()
        self.players: set[Player] = {}
        self.game_master: GameMaster = None
        self.participants: set = self.get_players().add(self.game_master)

    def add_player(self, player: Player):
        self.players.add(player)
        self._update_participants()

    def define_game_master(self, game_master: 'GameMaster'):
        if self.game_master == None:
            self.game_master = game_master
        else:
            raise ValueError(f'Game Master has already been declared.')

    def get_participants(self): return self.participants
    def get_players(self): return self.players
    def get_game_master(self): return self.game_master

    def _update_participants(self):
        if self.get_game_master():
            self.participants = self.get_players().add(self.get_game_master())
