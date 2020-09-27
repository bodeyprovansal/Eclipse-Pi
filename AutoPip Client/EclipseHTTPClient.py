import socket

class EclipseHTTPClient:
    def __init__(EC, host, port, msg_to_server):
        EC.host = host
        EC.port = port
        EC.msg_to_server = msg_to_server

        EC.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        EC.s.connect((EC.host, EC.port))
        EC.s.send(EC.msg_to_server)

        EC.msg_from_server = EC.s.recv(1024)
        EC.s.close()
        #print(EC.msg_from_server.decode('ascii'))
        

