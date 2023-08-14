# read an int from the user, check that it's a number
# from 5 to 100 (if so, print OK, else print ERROR)

MIN = 5
MAX = 100

text = input(F'enter a number between {MIN}-{MAX}: ')
# add checks that text can be converted to int
# CODE doesn't work for single digit!
if (text[0] == '-' and text[1:].isdigit()) or text.isdigit():
    print("yes, that's an int let's check range:")
    num = int(text)

    if MIN <= num <= MAX:
        print("OK")
    else:
        print(F"ERROR: not between {MIN} and {MAX}!")
else:
    print("ERROR: not an integer")
