import random

SECRET_NUMBER_MIN = 1
SECRET_NUMBER_MAX = 1000


def main():
    secret_number = random.randint(SECRET_NUMBER_MIN, SECRET_NUMBER_MAX)
    print(f"I'm thinking of a number between {SECRET_NUMBER_MIN} and {SECRET_NUMBER_MAX}")

    while True:
        guess_number = int(input('enter your guess:'))

        if guess_number < secret_number:
            print("too low")
        elif guess_number > secret_number:
            print("too high")
        else:
            print("correct!")
            break




if __name__ == '__main__':
    main()