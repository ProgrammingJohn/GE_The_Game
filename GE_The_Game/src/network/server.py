

import socket
import threading
import json


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))

    def listen_for_clients(self):
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Accepted connection from {address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break  # Client has disconnected
                message = data.decode('utf-8')
                print(f"Received from client: {message}")
                # Here you can process the message and perform actions based on it
                
                # For simplicity, we're just echoing back the received message
                response = f"Server received: {message}"
                client_socket.sendall(response.encode('utf-8'))
        finally:
            client_socket.close()

    def start(self):
        try:
            self.listen_for_clients()
        except KeyboardInterrupt:
            print("Server shutting down.")
        finally:
            self.server_socket.close()

# if __name__ == "__main__":
#     HOST, PORT = 'localhost', 9999
#     game_server = Server(HOST, PORT)
#     game_server.start()

    