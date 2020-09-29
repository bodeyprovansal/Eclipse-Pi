import socket, time

class EclipseHTTPClient:
    def __init__(EC, host, TCPport, devPort, command):
        EC.host = host
        EC.TCPport = TCPport
        EC.devPort = devPort
        #EC.command = command
        EC.command = 'DEV_PORT_START' + devPort + 'DEV_PORT_END' + command
        print("Sending Command: " + EC.command)

        EC.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        EC.s.connect((EC.host, EC.TCPport))
        EC.s.sendall(EC.command.encode('utf-8'))
        time.sleep(0.5)
        EC.response = EC.s.recv(1024)
        EC.s.close()
        #print(EC.msg_from_server.decode('ascii'))
    def getResponse(client):
            return client.response
    def setResponse(client, response):
            client.response = response
        

