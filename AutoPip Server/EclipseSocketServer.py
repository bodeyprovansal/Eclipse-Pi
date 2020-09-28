import http.server
import socketserver
import socket
from EclipseInterface import EclipseInterface


#s = 'asdf=5;iwantthis123jasd'
#print s[s.find(start)+len(start):s.rfind(end)]

class EclipseSocketServer():
    def __init__(self):
        serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
            
        host = socket.gethostname()
        
        port = 9090
        
        serversocket.bind((host, port))
        
        serversocket.listen(5)
        
        LOCAL_DEV_PORT_START = 'DEV_PORT_START'.encode('utf-8')
        LOCAL_DEV_PORT_END = 'DEV_PORT_END'.encode('utf-8')
        LOCAL_DEV_PORT = ''
        while True:
            clientsocket, addr = serversocket.accept()
            
            print("Got a connection from %s" % str(addr))
            
            msg_rec = clientsocket.recv(1024)
            LOCAL_DEV_PORT = msg_rec[msg_rec.find(LOCAL_DEV_PORT_START)+len(LOCAL_DEV_PORT_START):msg_rec.rfind(LOCAL_DEV_PORT_END)]
            msg_rec = msg_rec[msg_rec.find(LOCAL_DEV_PORT_END) + len(LOCAL_DEV_PORT_END):len(msg_rec)]
            
            #print("Message from client: " + msg_rec.decode('utf-8'))
            #msg_rec = msg_rec.decode('utf-8')
            print("Sending command to local port: " + LOCAL_DEV_PORT.decode('utf-8'))
            
            pip = EclipseInterface(LOCAL_DEV_PORT.decode('utf-8'), LOCAL_DEV_PORT.decode('utf-8'))
            pip.ser.write(bytes(msg_rec.decode('utf-8') + '\r', encoding='utf-8'))
            #pip.ser.write(bytes('\r'))
            msg_send = pip.readEclipse()
            
            clientsocket.sendall(msg_send)
            clientsocket.close()
            
        
    #def __init__(ES, port):
        #ES.Handler = http.server.SimpleHTTPRequestHandler
        #with socketserver.TCPServer(("", port), ES.Handler) as httpd:
            #print("serving at port", port)
            #httpd.serve_forever()
        
        
        
        #serv.s = socket.socket()
        #serv.s.bind(('', serv.port))
        #print ("socket binded to %s" %(serv.port))
        #serv.s.listen(5)
        #print ("socket is listening")
        
        #while True:
         #   serv.c, serv.addr = serv.s.accept()
          #  print ("Received connection from: ", serv.addr)
            
           # serv.c.send('Hello from server')
            #print (serv.c.recv(1024))
    
            #serv.c.close()
