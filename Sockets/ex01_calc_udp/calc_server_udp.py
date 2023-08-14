import socket
import json

SERVER_ADDRESS = '127.0.0.1', 54321


def main():
    with socket.socket(type=socket.SOCK_DGRAM) as s:
        s.bind(SERVER_ADDRESS)

        while True:
            req, addr = s.recvfrom(1024)
            resp = calculate_response(req)
            s.sendto(resp, addr)


def calculate_response(req: bytes) -> bytes:

    try:
        req = req.decode()
        req = json.loads(req)

        n1 = int(req['num1'])
        op = str(req['operation'])
        n2 = int(req['num2'])

    except UnicodeDecodeError:
        resp_str = 'error: not utf8'
    except json.JSONDecodeError:
        resp_str = 'error: not json'
    except KeyError:
        resp_str = 'error: invalid message'
    except TypeError:
        # if req is not dict or if n1/n2 not int
        # or if op not str etc...
        resp_str = 'error: invalid message'
    else:
        if op == '+':
            resp_str = str(n1 + n2)
        elif op == '-':
            resp_str = str(n1 - n2)
        elif op == '*':
            resp_str = str(n1 * n2)
        elif op == '/':
            if n2 == 0:
                resp_str = "error: cannot divide by zero"
            else:
                resp_str = str(n1 // n2)
        else:
            resp_str = "error: invalid operation"

    return resp_str.encode()


if __name__ == '__main__':
    main()