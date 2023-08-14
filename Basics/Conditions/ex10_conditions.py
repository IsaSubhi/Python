# read an int from the user, check that it's a number
# from 5 to 100 (if so, print OK, else print ERROR)

MIN = 5
MAX = 100

text = input(F'enter a number between {MIN}-{MAX}: ')

if not( (text[0] == '-' and text[1:].isdigit()) or text.isdigit() ):
    print("ERROR: not an integer")
    quit()

print("yes, that's an int let's check range:")
num = int(text)

# if not(MIN <= num <= MAX):
if num < MIN or num > MAX:
    print(F"ERROR: not between {MIN} and {MAX}!")
    quit()

print("OK")

