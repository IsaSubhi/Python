import random

SECRET_NUMBER_MIN = 1
SECRET_NUMBER_MAX = 10


def main():
    while True:
        secret_number = random.randint(SECRET_NUMBER_MIN, SECRET_NUMBER_MAX)
        print(f"I'm thinking of a number between {SECRET_NUMBER_MIN} and {SECRET_NUMBER_MAX}")

        while True:
            guess_number = input('enter your guess:')
            try:
                guess_number = int(guess_number)
            except ValueError:
                print("not an int!")
            else:
                if guess_number < secret_number:
                    print("too low")
                elif guess_number > secret_number:
                    print("too high")
                else:
                    print("correct!")
                    break

        print("generating a new random number")




if __name__ == '__main__':
    main()