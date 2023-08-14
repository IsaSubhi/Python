import socket

SERVER_ADDRESS = '127.0.0.1', 54321

client_list = []

with socket.socket() as accept_sock:

    accept_sock.bind(SERVER_ADDRESS)
    accept_sock.listen(16)
    print('server is listening at {}:{}'.format(*SERVER_ADDRESS))

    while True:
        client_sock, client_addr = accept_sock.accept()
        print("got connection from {}:{}".format(*client_addr))
        print("waiting for message ...")
        req = client_sock.recv(1024)
        print("got request: ", req)
        # here you compute response
        print("sending response:", req)
        client_sock.send(req)
        client_sock.close()
