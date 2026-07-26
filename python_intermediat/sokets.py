import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',55555))
s.listen()

while True:
    clinet , address = s.accept()
    print("connected to {}".format(address))
    clinet.send("you are conneted !".encode())
    clinet.close()