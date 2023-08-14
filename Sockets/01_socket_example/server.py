# echo server

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 54355))

while True:
    print("waiting for a request...")
    req, addr = s.recvfrom(1024)
    print(f"got from {addr} message: {req}")
    # transformation of req into response
    print("sending it back")
    s.sendto(req, addr)


