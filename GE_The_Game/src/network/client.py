

import socket
import json
import src.game_manager.state_manager.StateManager

PLAYER, GAME_MASTER = 'Player', 'Game Master'

class Client:
    def __init__(self, host, port):
        self.player_type_names = {PLAYER, GAME_MASTER}
        self.host, self.port = host, port

    def create_player(self, player_type: str):
        # Ensure player_type is either PlayerType1 or PlayerType2
        if player_type not in self._get_player_type_names():
            print(F"Invalid player type. Must be {PLAYER} or {GAME_MASTER}.")
            
            match player_type:
                case PLAYER: 
                case GAME_MASTER:

        # Connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.host, self.port))
                # Send the player type request to the server
                request = {'action': 'create_player', 'type': player_type}
                sock.sendall(json.dumps(request).encode('utf-8'))

                # Wait for the server's response
                response = sock.recv(1024).decode('utf-8')
                print(f"Server response: {response}")
            except ConnectionError as e:
                print(f"Connection error: {e}")


    


    def _get_player_type_names(self) -> set[str]: return self.player_type_names




# if __name__ == "__main__":
#     # Example usage
#     HOST, PORT = 'localhost', 9999
#     client = Client(HOST, PORT)

#     # Create a player of PlayerType1
#     client.create_player()

#     # Create a player of PlayerType2
#     client.create_player(GAME_MASTER)

        

    