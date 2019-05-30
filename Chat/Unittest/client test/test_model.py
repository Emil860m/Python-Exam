import unittest
import threading
import socket

import Chat.MVC.Model
import Chat.MVC.Controller
import Chat.Server.Server


class TestModel(unittest.TestCase):

    def run_fake_server(self):
        # Run a server to listen for a connection and then close it
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 50000))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    def test_client_connect(self):
        """Testing connecting the client to a server"""
        # Start fake server in background thread
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        # Test the clients basic connection and disconnection
        game_client = Chat.MVC.Model.Client(Chat.MVC.Controller.chatController)
        game_client.client_socket.close()

        # Ensure server thread ends
        server_thread.join()




if __name__ == "__main__":
    unittest.main()
