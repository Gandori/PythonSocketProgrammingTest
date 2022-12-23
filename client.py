import socket

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

msg = s.recv(1024)

print('Received:' + msg.decode())

s.close()