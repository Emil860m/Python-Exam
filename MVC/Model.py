import socket
import threading


class Client:
    def receive(self):
        while self.alive == 1:
            data = self.conn.recv(1024)
            if not data:
                continue
            self.controller.receive(data.decode())
            # print(data.decode())

    def __init__(self, controller):
        self.alive = 1

        self.controller = controller

        # self.IP = input("Enter IP of the server: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 50000))
        # s.send(input("Enter username: ").encode())
        new_port = int(s.recv(1024).decode())
        s.close()

        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(('localhost', new_port))

        # t1 = threading.Thread(target=send)
        self.t2 = threading.Thread(target=self.receive)
        print("Connected to chat")
        # t1.start()
        self.t2.start()

    def send(self, msg):
        while True:
            # msg = input()
            self.conn.send(msg.encode())
