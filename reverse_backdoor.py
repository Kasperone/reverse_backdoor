#!/usr/bin/ env python
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("xx.x.x.xx", 4444))

connection.send("\n[+] Connection established.\n")

received_data = connection.recv(1024)
print(received_data)

connection.close()