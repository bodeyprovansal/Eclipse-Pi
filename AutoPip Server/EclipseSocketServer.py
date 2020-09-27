import http.server
import socketserver
import socket

class EclipseSocketServer():
    def __init__(self):
        serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
            
        host = socket.gethostname()
        
        port = 9090
        
        serversocket.bind((host, port))
        
        serversocket.listen(5)
        
        while True:
            clientsocket, addr = serversocket.accept()
            
            print("Got a connection from %s" % str(addr))
            msg_from_client = clientsocket.recv(1024)
            print("Message from client: " + msg_from_client.decode('ascii'))
            msg_to_client = 'Connection succesful' + "\r\n"
            clientsocket.send(msg_to_client.encode('ascii'))
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
