import socket

SERVER_ADDRESS = ('127.0.0.1', 54321)
MIN = 1
MAX = 1000
RECV_WINDOW = 1024




def main():
    print(f"I'm thinking of a number between {MIN} and {MAX}:")

    # guessing loop
    while True:
        guess = input('enter guess:')

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(guess.encode(), SERVER_ADDRESS)

            # recv until you recv form server
            while True:
                response, addr = s.recvfrom(RECV_WINDOW)
                if addr == SERVER_ADDRESS:
                    break
                else:
                    print("ignoring non-server response")

        response = response.decode()
        message = response_to_message(response)
        print(message)


def response_to_message(response):
    """
    converts server response to a simple message
    to print for the client end-user
    """
    if response == 'too low':
        return 'number is too low'
    elif response == 'too high':
        return 'number is too high'
    elif response == 'cannot decode':
        return 'could not decode to UTF8'
    elif response == 'could not parse int':
        return 'error: not an int'
    elif response == 'equals':
        return 'correct! guessing another number'
    else:
        return f'unknown response: {response}'

if __name__ == '__main__':
    main()