import random

# CONSTANTS
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES = 5

# MAIN
def main():
    # main loop
    while True:
        # generate a random number
        secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        tries = MAX_TRIES

        print(f"I'm thinking of a number between {MIN_NUMBER}"
              f" and {MAX_NUMBER}. You have {MAX_TRIES} tries.")

        # game loop
        while tries > 0:
            #   ask the player to guess the number
            guess_number = int(input('guess: '))

            # TODO: check if int conversion didn't fail (learn about exceptions first)

            # if guess_number < MIN_NUMBER or guess_number > MAX_NUMBER:
            # if not(MIN_NUMBER <= guess_number <= MAX_NUMBER):
            if guess_number not in range(MIN_NUMBER, MAX_NUMBER + 1):
                print(f"error: nubmer must be between {MIN_NUMBER} and {MAX_NUMBER}")

            # check results
            elif guess_number < secret_number:
                print("too low")
                tries -= 1
            elif guess_number > secret_number:
                print("too high")
                tries -= 1
            else:
                print("that's right!")
                break # break the game loop

        if tries <= 0:
            print(f"game over! no more tries left. the correct "
                  f"number was {secret_number}")
        else:
            print("you win")

        answer = input("would you like to play again? (enter 'y' for yes, anything else for no):")
        answer = answer.lower()
        if answer != 'y':
            break # break the main loop

if __name__ == '__main__':
    main()