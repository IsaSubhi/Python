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
        print(response)
        # if response == 'too low':
        #     print('number is too low')
        # elif response == 'too high':
        #     print('number is too high')
        # elif response == 'cannot decode':
        #     print('could not decode to UTF8')
        # elif response == 'could not parse int':
        #     print('error: not an int')
        # elif response == 'equals':
        #     print('correct! guessing another number')
        # else:
        #     print(f'unkown response: {response}')

if __name__ == '__main__':
    main()