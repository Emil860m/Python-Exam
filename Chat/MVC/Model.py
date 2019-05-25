from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class Client:

    def send_msg(self, msg):
        """Sends the messages to the server"""
        self.client_socket.send(msg.encode())
        if msg == "{quit}":
            self.client_socket.close()
            self.controller.quit()
            self.alive = False

    def receive_msg(self):
        """Infinite loop that receives messages from the server"""
        while self.alive:
            try:
                msg = self.client_socket.recv(1024)
                self.controller.msg_received(msg)
            except OSError:
                break

    def __init__(self, controller):
        """Constructor creating the connection to the server"""
        self.alive = True

        self.controller = controller

        HOST = '127.0.0.1'
        PORT = 50000

        ADDR = (HOST, PORT)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)

        self.receive_thread = Thread(target=self.receive_msg)
        self.receive_thread.start()
