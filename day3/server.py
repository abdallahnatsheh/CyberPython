import socket

s = socket.socket() # socket creation
host = socket.gethostname()
port = 12345

s.bind((host,port))   #bind host and port
s.listen(5)

while True:
    channel,address= s.accept()
    print("the connection from : ",address)
   # channel.send(b"thanks for connecting")
    channel.sendall("thanks for connecting".encode("utf-8"))
    channel.close()


