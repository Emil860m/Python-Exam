import socket
from socket import SHUT_WR

"""
This file contains the different commands available in the chat.
"""
commands = {
    "/w": "private_msg",
    "/quit": "client_disconnect",
    "/file": "handle_file",
    "/filesend": "send_file"
}

"""The parameter brought on from the method call is list containing: 
0: clients; A list of clients
1: client; The client sending the message
2: msg; The message send
3: name: The name of the sender
"""


def private_msg(para):
    """For sending massages to one specific chat member"""
    receiver_name = ""
    receiver = ""
    clients = para[0]
    client = para[1]
    msg = para[2]
    whisper_to = msg.split()[1]
    name = para[3]
    # print(clients)
    for c in clients:
        if whisper_to == clients[c]:
            receiver_name = clients[c]
            receiver = c
            msg = msg[len(whisper_to) + 4:]
    if receiver != "":
        client.send(("You whisper " + receiver_name + ": " + msg).encode())
        receiver.send((name + " whispers: " + msg).encode())
    else:
        client.send(("Chatter \'" + msg.split()[1] + "\' does not exist.").encode())


def client_disconnect(para):
    """Handles when a client disconnects"""
    clients = para[0]
    client = para[1]
    print(clients[client] + " disconnected")
    del clients[client]


def handle_file(para):
    """Handles receiving a file"""
    msg = para[2]
    filename = msg.split()[1]
    clients = para[0]
    client = para[1]
    print(filename)
    temp_socket = socket.socket()
    host = "127.0.0.1"
    port = 12345
    temp_socket.bind((host, port))
    temp_socket.listen(0)
    print("listening")
    c, addr = temp_socket.accept()
    print("connected")
    f = open("C:/Users/amxur/Desktop/Python-exam/Python-Exam/Chat/Server/Files/" + filename, "wb+")
    l = c.recv(1024)
    while l:
        f.write(l)
        l = c.recv(1024)
    print("done receiving")
    for s in clients:
        s.send(("/file " + clients[client] + " send a file: " + filename).encode())
    f.close()
    c.close()


def send_file(para):
    print("File requested")
    msg = para[2]
    filename = "C:/Users/amxur/Desktop/Python-exam/Python-Exam/Chat/Server/Files/" + msg.split()[1]
    temp_socket = socket.socket()
    temp_socket.bind(("127.0.0.1", 12346))
    temp_socket.listen(0)
    c, addr = temp_socket.accept()
    f = open(filename, "rb")
    l = f.read(1024)
    print("Sending file")
    while l:
        c.send(l)
        l = f.read(1024)
    print("Done sending file")
    c.shutdown(SHUT_WR)
    f.close()
    c.close()


