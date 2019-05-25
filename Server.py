import socket
import threading
import User


def send_to_all(data):
    for k in conn_list.keys():
        conn_list[k].send(data)


def send_and_receive(name):
    while True:
        data = conn_list[name].recv(1024)
        # print(data.decode())
        if not data:
            print("dead")
            break
        if data.decode() != '{quit}':
            file = open("chat.txt", "a+")
            file.write(name + ": " + data.decode() + "\n")
            file.close()
            send_to_all(name.encode() + ": ".encode() + data)
        else:
            conn_list[name].close()
            print(name + " disconnected.")
            conn_list.pop(name)
            print("Connected Users: " + conn_list)


conn_list = {}
PORT = 50000
localPort = 50001
if __name__ == "__main__":
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', PORT))
        s.listen()
        conn, addr = s.accept()

        conn.send(str(localPort).encode())
        user_name = conn.recv(1024).decode()

        s.close()
        conn.close()

        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ls.bind(('localhost', localPort))
        ls.listen()
        conn, addr = ls.accept()
        localPort += 1

        f = open("chat.txt", "r")
        for i in f:
            conn.send(i.encode())
        conn.send("Connected. Send {quit} to quit".encode())
        conn.send("\n".encode())
        f.close()

        conn_list[user_name] = conn
        print("Connected: ", addr)
        t1 = threading.Thread(target=send_and_receive, args=(user_name,))
        t1.start()
