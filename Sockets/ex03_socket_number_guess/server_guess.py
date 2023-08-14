import socket
import random

SERVER_ADDRESS = ('127.0.0.1', 54321)
MIN = 1
MAX = 1000
RECV_WINDOW = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        # server initialization
        s.bind(SERVER_ADDRESS)
        print('server is now listening at {}:{}...'.format(
            *SERVER_ADDRESS
        ))

        secret_number = random.randint(MIN, MAX)

        while True:
            print('waiting for request')
            req, client_addr = s.recvfrom(RECV_WINDOW)

            print('received from {}:{} message: "{}"'.format(
                *client_addr, req
            ))

            res = compute_response(req, secret_number)
            s.sendto(res.encode(), client_addr)


def compute_response(req, secret_number):
    """
    :param req: bytes of the request of the user
    :param secret_number: the current secret number
    :return: string response for the request
    """
    try:
        req = req.decode()
        guess_number = int(req)
    except UnicodeDecodeError:
        res = 'cannot decode'
    except ValueError:
        res = 'could not parse int'
    else:
        if guess_number < secret_number:
            res = "too low"
        elif guess_number > secret_number:
            res = "too high"
        else:
            res = "equals"
            secret_number = random.randint(MIN, MAX)

    return res


if __name__ == '__main__':
    main()