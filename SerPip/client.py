#!/usr/bin/env python
import socket
import sys

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket created"
except socket.error as err:
    print "socket was not created, failed with error %s" %(err)

port = 12345

s.connect(('127.0.0.1', port))
print s.recv(1024)

s.send('hello from client')

s.close()
