"""
This file contains the different commands available in the chat.
"""
commands = {
    "/w": "private_msg",
    "/quit": "client_disconnect"
}

"""The parameter brought on from the method call is list containing: 
0: clients; A list of clients
1: client; The client sending the message
2: msg; The message send
"""


def private_msg(para):
    """For sending massages to one specific chat member"""
    name = ""
    receiver = ""
    clients = para[0]
    client = para[1]
    msg = para[2]
    whisper_to = msg.split()[1]
    # print(clients)
    for c in clients:
        #  todo: bug when 2nd client connected tries to whisper. makes no sense
        if whisper_to == clients[c]:
            name = clients[c]
            receiver = c
            msg = msg[len(whisper_to) + 4:]
    if receiver != "":
        client.send(("You whisper " + name + ": " + msg).encode())
        receiver.send((clients[client] + " whispers: " + msg).encode())
    else:
        client.send(("Chatter \'" + msg.split()[1] + "\' does not exist.").encode())


def client_disconnect(para):
    """Handles when a client disconnects"""
    clients = para[0]
    client = para[1]
    print(clients[client] + " disconnected")
    del clients[client]
