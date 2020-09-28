import socket

class EclipseHTTPClient:
    def __init__(EC, host, TCPport, devPort, command):
        EC.host = host
        EC.TCPport = TCPport
        EC.devPort = devPort
        #EC.command = command
        EC.command = 'DEV_PORT_START' + devPort + 'DEV_PORT_END' + command
        print("Sending Command: " + command)

        EC.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        EC.s.connect((EC.host, EC.TCPport))
        EC.s.sendall(EC.command.encode('utf-8'))

        EC.msg_from_server = EC.s.recv(1024)
        EC.s.close()
        #print(EC.msg_from_server.decode('ascii'))
        

