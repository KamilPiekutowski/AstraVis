#!/usr/bin/python

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
	if buf == 'test':
		print 'test sucessfull.'
	elif buf == 'quit':
		print 'Closing server...'
		print 'Done!'
    		break
	else:
		print 'Unknown command: %s' % buf
