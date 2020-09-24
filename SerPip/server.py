#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import socket

port = 12345
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
s = socket.socket()
s.bind(('',port))
print "socket binded to %s" %(port)
s.listen(5)
print "socket is listening"

while True:
    c, addr = s.accept()
    print "got connection from", addr
    
    c.send('Hello from server')
    print c.recv(1024)
    
    c.close()

#httpd =  SocketServer.TCPServer(("", PORT), Handler)

#print("serving at port", PORT)

#httpd.serve_forever()

