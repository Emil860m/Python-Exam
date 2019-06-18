from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from socket import SHUT_WR

import Chat.MVC.protocol


class Client:

    def send_msg(self, msg):
        """Sends the messages to the server"""
        self.client_socket.send(msg.encode())
        if msg == "/quit":
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

    def send_file(self, filename):
        file = filename.split("/")
        file = file[len(file)-1]
        self.send_msg("/file " + file)
        temp_socket = socket(AF_INET, SOCK_STREAM)
        temp_socket.connect(("127.0.0.1", 12345))
        f = open(filename, "rb")
        l = f.read(1024)
        while l:
            temp_socket.send(l)
            l = f.read(1024)
        f.close()
        temp_socket.shutdown(SHUT_WR)
        temp_socket.close()



    def receive_file(self, filename):
        self.send_msg("/filesend " + filename)
        temp_socket = socket(AF_INET, SOCK_STREAM)
        temp_socket.connect(("127.0.0.1", 12346))
        f = open("C:/Users/amxur/Desktop/Python-exam/Python-Exam/Chat/MVC/files/" + filename, "wb+")
        l = temp_socket.recv(1024)
        while l:
            f.write(l)
            l = temp_socket.recv(1024)
        f.close()
        temp_socket.close()


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
