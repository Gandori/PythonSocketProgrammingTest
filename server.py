import socket

HOST = 'localhost'
PORT = 5000
MAXCONNECTIONS = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', PORT))

s.listen(MAXCONNECTIONS)

c, addr = s.accept()

print(f"Connection From: {str(addr)}")

c.send(b'HelloWorld')

c.close()

