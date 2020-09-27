import SimpleHTTPServer
import SocketServer
import socket

class EclipseHTTPServer:
    def __init__(serv, name, port, ip):
        serv.name = name
        serv.port = port
        serv.ip = ip
        
        serv.Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        serv.s = socket.socket()
        serv.s.bind(('', serv.port))
        print "socket binded to %s" %(serv.port)
        serv.s.listen(5)
        print "socket is listening"
        
        while True:
            serv.c, serv.addr = serv.s.accept()
            print "Received connection from: ", serv.addr
            
            serv.c.send('Hello from server')
            print serv.c.recv(1024)
    
            serv.c.close()
