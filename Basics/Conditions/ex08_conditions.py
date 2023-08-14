# read an int from the user, check that it's a number
# from 5 to 100 (if so, print OK, else print ERROR)

text = input('enter a number between 5-100: ')
# add checks that text can be converted to int
# CODE doesn't work for single digit!
if (text[0] == '-' and text[1:].isdigit()) or text.isdigit():
    print("yes, that's an int let's check range:")
    num = int(text)

    if 5 <= num <= 100:
        print("OK")
    else:
        print("ERROR: not between 5 and 100!")
else:
    print("ERROR: not an integer")
