import socket

#socket.setdefaulttimeout(0.5)
socket.setdefaulttimeout(0)

SERVER_ADDRESS = ('127.0.0.1', 54321)
BUFFER_SIZE = 1024

clients = []

with socket.socket() as server:

    server.bind(SERVER_ADDRESS)
    server.listen(16)

    print("server is listening at {}:{}".format(*SERVER_ADDRESS))

    # loop for accepting new clients and receiving responses
    while True:

        try:
            client_sock, client_addr = server.accept()
        except (socket.timeout, BlockingIOError):
            pass
        else:
            print("client connected from {}:{}".format(*client_addr))
            clients.append(client_sock)

        for client in clients.copy():

            try:
                data = client.recv(BUFFER_SIZE)

            except (socket.timeout, BlockingIOError):
                pass

            except OSError:
                print("client {}:{} crashed".format(*client.getpeername()))
                clients.remove(client)

            else:
                if len(data) == 0: #client closed
                    print("client {}:{} closed".format(*client.getpeername()))
                    clients.remove(client)
                else:
                    text = data.decode()
                    n1, op, n2 = text.split()
                    n1 = int(n1)
                    n2 = int(n2)

                    if op == '+':
                        resp = str(n1 + n2)
                    elif op == '-':
                        resp = str(n1 - n2)
                    # ...
                    else:
                        resp = 'operator not supported'

                    client.send(resp.encode())
















