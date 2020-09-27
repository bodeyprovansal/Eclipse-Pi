import http.server
import socketserver

class EclipseHTTPServer(socketserver.StreamRequestHandler):
    def handle(self):
        print("Received one request from {}".format(self.client_address[0]))
        msg = self.rfile.readline().strip()
        print("Data Received from client:".format(msg))
        print(msg)
        
        self.wfile.write("Hello Client....Received Message".encode())
        
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
