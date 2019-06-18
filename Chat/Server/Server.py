from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

import Chat.Server.protocol


class Server:
    def accept_incoming_connections(self):
        """Sets up handling for incoming clients."""
        while True:
            client, client_address = self.SERVER.accept()
            print("%s:%s has connected." % client_address)
            client.send("Welcome to the chat. Please enter your name!".encode())
            self.addresses[client] = client_address
            Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):  # Takes client socket as argument.
        """Handles a single client connection."""
        name = client.recv(self.BUFSIZ).decode("utf8")
        welcome = 'Welcome %s! If you ever want to quit, type /quit to exit.' % name
        client.send(welcome.encode())
        msg = "%s has joined the chat!" % name
        self.broadcast(msg.encode())
        self.clients[client] = name
        """While loop for receiving, handling and sending messages"""
        while True:
            try:
                msg = client.recv(self.BUFSIZ)
            except OSError:
                break
            decoded_msg = msg.decode()
            """This checks if you have attempted to enter a command f.x. /w or /quit. 
            It will then check if it exists. if yes, it will call the right method from the json file"""
            if decoded_msg[0] == "/":
                command = decoded_msg.split()[0]
                parameter_list = [self.clients, client, decoded_msg, name]
                try:
                    getattr(Chat.Server.protocol, self.protocol[command])(parameter_list)
                except KeyError:
                    client.send(("The command " + command + " does not exist").encode())
            else:
                self.broadcast(msg, name + ": ")

    def broadcast(self, msg, prefix=""):  # prefix is for name identification.
        """Broadcasts a message to all the clients."""
        for s in self.clients:
            s.send(prefix.encode() + msg)

    def __init__(self):
        self.clients = {}

        self.addresses = {}

        HOST = ''
        PORT = 50000

        self.BUFSIZ = 1024
        ADDR = (HOST, PORT)
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(ADDR)
        """This python file contains the different functions and their method calls. 
            Whenever a new method is implemented put the key as the protocol and method call as value"""
        self.protocol = Chat.Server.protocol.commands

        self.SERVER.listen(5)
        print("Waiting for connection...")
        ACCEPT_THREAD = Thread(target=self.accept_incoming_connections)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        self.SERVER.close()
