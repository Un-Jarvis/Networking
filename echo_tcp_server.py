import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # check whether the string contains the secret code
        if "SECRET" in self.data:
            # return all the digits in the string and the total number of digits
            digits = ""
            for c in list(self.data):
                if c.isdigit():
                    digits += str(c)
            self.request.sendall("Digits: " + digits + " Count: " + str(len(digits)))
        else:
            # return not found
            self.request.sendall("Secret code not found.")
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

HOST, PORT = "localhost", 5000

# Create the server, binding to localhost on port 9999
server = socketserver.TCPServer((HOST, PORT), TCPHandler)
# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
server.serve_forever()