import socket
import json


SERVER_ADDRESS = '127.0.0.1', 58585


class Session:
    MAX_REQUESTS = 3

    def __init__(self, addr, sock):
        self.addr = addr
        self.sock = sock
        self.requests_left = Session.MAX_REQUESTS


def main():
    socket.setdefaulttimeout(0)

    # session_dict = {}  # {addr : Session}
    session_dict: dict[tuple[str, int]: Session] = {}

    with socket.socket() as accept_sock:
        accept_sock.bind(SERVER_ADDRESS)
        accept_sock.listen(16)

        print("server is listening at {}:{}".format(*SERVER_ADDRESS))

        # server loop
        while True:
            try:
                client_sock, client_addr = accept_sock.accept()
                print("new client: {}:{}".format(*client_addr))
            except BlockingIOError:
                pass
            except TimeoutError:
                pass
            else:
                new_session = Session(client_addr, client_sock)
                session_dict[client_addr] = new_session

            for session in session_dict.copy().values():

                try:
                    req = session.sock.recv(1024)
                    print("{}:{} -> {}".format(*session.addr, req))
                except BlockingIOError:
                    pass
                except TimeoutError:
                    pass
                else:
                    # if client "disconnected":
                    if req == b'':
                        session.sock.close()
                        del session_dict[session.addr]
                        print("client disconnected {}:{}".format(*session.addr))

                    # else client has a request:
                    else:
                        resp = calculate_response(req, session)
                        print('response to {}:{} -> {}'.format(*session.addr, resp))
                        session.sock.send(resp)


def calculate_response(req: bytes, session) -> bytes:
    if session.requests_left == 0:
        return 'error: out of requests'.encode()
    else:
        session.requests_left -= 1

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