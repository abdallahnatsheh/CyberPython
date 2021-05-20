import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))  # connect with host throught port
data = s.recv(1024)
print(data)
s.close()
