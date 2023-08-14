# read an int from the user, check that it's a number
# from 1 to 100 (if so, print OK, else print ERROR)

text = input('enter a number between 1-100: ')
# add checks that text can be converted to int
# doesn't work for negative
if text.isdigit():
    num = int(text)

    if 1 <= num <= 100:
        print("OK")
    else:
        print("ERROR: not between 1 and 100!")
else:
    print("ERROR: not an integer")
