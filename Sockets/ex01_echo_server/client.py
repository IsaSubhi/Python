
import socket
SERVER_ADDRESS = '127.0.0.1', 54323
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind( ('127.0.0.1', 54322))

try:
    while True:
        message = input("enter message to send:")  # blocking
        s.sendto(message.encode(), SERVER_ADDRESS)

        response, addr = s.recvfrom(1024)  # blocking
        print("got back:")
        print(response.decode())
finally:
    s.close()




