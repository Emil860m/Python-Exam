from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
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
        if decoded_msg[:3] == "/w ":
            chatter = decoded_msg.split()[1]
            # decoded_msg = decoded_msg[3:]
            chatterbool = False
            for c in clients:
                if chatter == clients[c]:
                    decoded_msg = decoded_msg[len(chatter) + 4:]
                    private_msg(name + " whispers: " + decoded_msg, c)
                    chatterbool = True
            if not chatterbool:
                client.send(("The chatter \'" + chatter + "\' does not exist").encode())
        elif msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            try:
                client.send(bytes("{quit}", "utf8"))
                client.close()
            except OSError:
                pass
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


def private_msg(msg, receiver):
    """For sending massages to one specific chat member"""
    receiver.send(msg.encode())


clients = {}
addresses = {}

HOST = ''
PORT = 50000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
