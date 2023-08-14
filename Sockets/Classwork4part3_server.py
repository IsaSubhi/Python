import socket as socket_library

GLOBAL_ADDRESS=("192.168.31.170", 62340)
BUFFER_SIZE=pow(2, 10)
server_socket=socket_library.socket(family=socket_library.AF_INET,
                                    type=socket_library.SOCK_STREAM)
server_socket.bind(GLOBAL_ADDRESS)
server_socket.listen(2)
server_socket.settimeout(3)
clients={}
print("The server is listening to the clients.")
while True:
    try:
        client, address=server_socket.accept()
        if client not in clients:
            clients[client]=address
            client.settimeout(3)
    except socket_library.timeout:
        print("No connection from clients. Timed out.")
    del_keys=list()
    for key in clients:
        try:
            print("Received \""+key.recv(BUFFER_SIZE).decode()+"\"from", clients[key])
            key.send("Thank you for connection.".encode())
        except socket_library.timeout:
            print("No message from:", clients[key])
        except ConnectionError:
            print(f"{clients[key]} is disconnected.")
            del_keys.append(key)
    for i in del_keys:
        del clients[i]