import socket

RES_TOO_LOW = 0
RES_TOO_HIGH = 1
RES_EQUALS = 2


SERVER_ADDRESS = ('127.0.0.1', 54321)
MIN = 1
MAX = 1000
RECV_WINDOW = 1024




def main():
    print(f"I'm thinking of a number between {MIN} and {MAX}:")

    # guessing loop
    while True:
        guess = int(input('enter guess:'))

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

            s.sendto(guess.to_bytes(2, 'big'), SERVER_ADDRESS)

            # recv until you recv form server
            while True:
                response, addr = s.recvfrom(RECV_WINDOW)
                if addr == SERVER_ADDRESS:
                    break
                else:
                    print("ignoring non-server response")

        message = response_to_message(response)
        print(message)


def response_to_message(response):
    """
    converts server response (bytes) to a simple message
    to print for the client end-user
    """

    response_number = int.from_bytes(response, 'big')

    if response_number == RES_TOO_LOW:
        return 'number is too low'
    elif response_number == RES_TOO_HIGH:
        return 'number is too high'
    elif response_number == RES_EQUALS:
        return 'correct! guessing another number'
    else:
        return f'unknown response: {response}'


if __name__ == '__main__':
    main()