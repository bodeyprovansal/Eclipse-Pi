import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 9090
s.connect(("192.168.1.172", port))

msg = s.recv(1024)

s.close()
print(msg.decode('ascii'))
#request = "Client Request for Host: %s" %target_h


