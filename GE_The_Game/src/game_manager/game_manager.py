

from src.game_manager.state_manager import StateManager
from src.network.network_handler import NetworkHandler
from src.players.player import Player
from src.network.client import Client
from src.network.server import Server


class GameManager():

    def __init__(self):

        self.state_manager = StateManager()
        self.network_handler = NetworkHandler()
        self.client_players = []
        self.server = Server()

    def select_role(self):
        role = input('Choose a role: "Player" or "Game Master."') #Once a connection is reached, then make a choice between what player type will be chosen.
        self.add_client_player(role)

    def add_client_player(self, role: str):
        client = Client()
        player = client.add_client()
        self.client_players.append(player)

    def start_server(self): self.server.start()

    def run(self):

        while True:
            self.start_server()
            self.select_role()



            
    
            