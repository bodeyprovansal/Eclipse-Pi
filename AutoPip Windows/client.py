import socket
import sys

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket created")
except socket.error as err:
    print ("socket was not created, failed with error %s" %(err))

port = 12345

s.connect(('192.168.1.188', port))
print (s.recv(1024))

s.send(bytes('hello from client', 'utf-8'))

s.close()