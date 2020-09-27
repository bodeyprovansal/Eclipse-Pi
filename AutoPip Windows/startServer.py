import socketserver
from EclipseHTTPServer import EclipseHTTPServer
from EclipseSocketServer import EclipseSocketServer
#newServer = EclipseHTTPServer(12345)

#aServer = socketserver.TCPServer(("127.0.0.1", 9090), EclipseHTTPServer)

#aServer.serve_forever()

sockServer = EclipseSocketServer()