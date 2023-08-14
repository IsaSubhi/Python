import random

# CONSTANTS
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES = 5


# MAIN
def main():
    # generate a random number
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    tries = MAX_TRIES

    print(f"I'm thinking of a number between {MIN_NUMBER}"
          f" and {MAX_NUMBER}. You have {MAX_TRIES} tries.")

    while tries > 0:
        #   ask the player to guess the number
        guess_number = int(input('guess: '))

        #   check results
        if guess_number < secret_number:
            print("too low")
            tries -= 1
        elif guess_number > secret_number:
            print("too high")
            tries -= 1
        else:
            print("that's right!")
            break

    if tries <= 0:
        print(f"game over! no more tries left. the correct "
              f"number was {secret_number}")
    else:
        print("you win")


if __name__ == '__main__':
    main()








