import socket
import threading

def send(event=None):
    while True:
        data = input()
        s.send(data.encode())



def receive():
    while True:
        data = s.recv(1024)
        if not data:
            continue
        print(data.decode())



IP = input("Enter IP of the server: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, 50000))
s.send(input("Enter username: ").encode())
new_port = int(s.recv(1024).decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', new_port))

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)
print("Connected to chat")
t1.start()
t2.start()
