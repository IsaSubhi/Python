# technique UDP-IP. The Client
import socket as socket_library
import time as time_library

HOST_ADDRESS=("192.168.31.170", 61761)
number=1
BUFFER_SIZE=pow(2, 10)
client_socket=socket_library.socket(family=socket_library.AF_INET,
                                    type=socket_library.SOCK_DGRAM)
client_socket.sendto("Hello server.".encode(encoding="UTF-8"), HOST_ADDRESS)
while number<6:
    message, address=client_socket.recvfrom(BUFFER_SIZE)
    print("Received message from server \""+message.decode(encoding="UTF-8")+"\"")
    client_socket.sendto(f"Client1. Message {number}".encode(), HOST_ADDRESS)
    number+=1
    time_library.sleep(4)
client_socket.close()