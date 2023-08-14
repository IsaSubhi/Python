import socket
import json

SERVER_ADDRESS = '127.0.0.1', 58585


def main():
    with socket.socket() as s:

        s.connect(SERVER_ADDRESS)

        while True:
            # for simplicity input should be space separated
            equation_string = input("enter equation (space separated):")

            if equation_string.lower() == 'quit':
                break

            # TODO: check input validity etc.
            n1, op, n2 = equation_string.split()
            equation = {
                'num1': int(n1),
                'operation': op,
                'num2': int(n2)
            }
            req = json.dumps(equation).encode()

            s.send(req)
            # naively assuming the recv will come from the server
            resp = s.recv(1024)
            print("result: ", resp.decode())


if __name__ == '__main__':
    main()
