#!/usr/bin/python
import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
if len(sys.argv) < 2:
	clientsocket.send('quit')
else:
	clientsocket.send(sys.argv[1])

