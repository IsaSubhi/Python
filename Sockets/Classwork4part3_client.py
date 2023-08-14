import socket as socket_library
import time as time_library

class Client:
    GLOBAL_ADDRESS = ("192.168.31.170", 62340)
    BUFFER_SIZE = pow(2, 10)
    def __init__(self, n):
        self.n=n
        self.number=1
        self.client_socket=socket_library.socket()

    def action(self):
        try:
            self.client_socket.connect(Client.GLOBAL_ADDRESS)
        except ConnectionError:
            print("The server is not available.")
            self.client_socket.close()
            exit()
        else:
            self.client_socket.send("Hello server".encode())
            self.client_socket.settimeout(3)
            while self.number<6:
                try:
                    print("Received from server \""+self.client_socket.recv(Client.BUFFER_SIZE).decode()+"\"")
                    self.client_socket.send(f"Client{self.n}. Message {self.number}".encode())
                    self.number+=1
                    time_library.sleep(0)
                except socket_library.timeout:
                    print("The server is not responding.")
                    break
        self.client_socket.close()


if __name__=="__main__":
    clients=[]
    for i in range(6):
        clients.append(Client(i+1))
        clients[i].action()