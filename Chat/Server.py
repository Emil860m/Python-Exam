from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import json


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to the chat. Please enter your name!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type /quit to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        try:
            msg = client.recv(BUFSIZ)
        except OSError:
            break
        decoded_msg = msg.decode()
        """This checks if you have attempted to enter a command like /w or /quit. 
        It will then check if it exists. if yes, it will call the right method from the json file"""
        if decoded_msg[0] == "/":
            command = decoded_msg.split()[0]
            command_available = False
            for x in protocol.keys():
                if command == x:
                    """All methods called from this json file
                     requires the client and the decoded message as parameters"""
                    command_available = True
                    globals()[protocol[x]](client, decoded_msg)
                    break
            if not command_available:
                client.send(("The command " + command + " does not exist").encode())
        else:
            broadcast(msg, name + ": ")


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


def private_msg(client, msg):
    """For sending massages to one specific chat member"""
    name = ""
    receiver = ""
    for c in clients:
        if msg.split()[1] == clients[c]:
            name = clients[c]
            receiver = c
            msg = msg[len(msg.split()[1]) + 4:]
    try:
        client.send((name + " whispers: " + msg).encode())
        receiver.send((name + " whispers: " + msg).encode())
    except AttributeError:
        client.send(("Chatter \'" + msg.split()[1] + "\' does not exist.").encode())


def client_disconnect(client, msg):
    try:
        print(clients[client] + " disconnected")
        client.close()
    except OSError:
        print("Error")
    del clients[client]


clients = {}
addresses = {}

HOST = ''
PORT = 50000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

with open('.protocol.json') as protocol_file:
    """This json file contains the different functions and their method calls. 
    Whenever a new method is implemented put the key as the protocol and method call as value"""
    protocol = json.load(protocol_file)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
