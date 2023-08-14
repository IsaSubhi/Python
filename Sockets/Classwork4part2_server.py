# technique UDP-IP. The server
import socket as socket_library

port=61761
BUFFER_SIZE=pow(2, 10)
server_socket=socket_library.socket(family=socket_library.AF_INET,
                                    type=socket_library.SOCK_DGRAM)
# server_socket.bind(('*', port))
server_socket.bind(("192.168.31.170", port))
print("Server is listening.")
while True:
    try:
        message, address=server_socket.recvfrom(BUFFER_SIZE)
    except ConnectionError:
        print("Connection with the server is closed now!")
        server_socket.close()
        break
    else:
        print("Received \""+message.decode()+"\" from", address)
        server_socket.sendto("Thank you for connection.".encode(), address)