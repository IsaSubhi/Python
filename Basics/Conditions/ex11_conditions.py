# read an int from the user, check that it's a number
# from 5 to 100 (if so, print OK, else print ERROR)

MIN = 5
MAX = 100

text = input(F'enter a number between {MIN}-{MAX}: ')

is_minus_and_digits = (text[0] == '-' and text[1:].isdigit())
is_all_digits = text.isdigit()
is_valid_int = is_minus_and_digits or is_all_digits

if not is_valid_int:
    print("ERROR: not an integer")
    quit()

print("yes, that's an int let's check range:")
num = int(text)

# if not(MIN <= num <= MAX):
if num < MIN or num > MAX:
    print(F"ERROR: not between {MIN} and {MAX}!")
    quit()

print("OK")

