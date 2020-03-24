import socket
import sys

HOST, PORT = "localhost", 5000
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
sock.sendall(bytes(data + "\n"))

# Receive data from the server and shut down
received = str(sock.recv(1024))

print("Sent:     {}".format(data))
print("Received: {}".format(received))