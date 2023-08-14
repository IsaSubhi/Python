# read an int from the user, check that it's a number
# from 1 to 100 (if so, print OK, else print ERROR)

num = int(input('enter a number between 1-100: '))

if 1 <= num <= 100:
    print("OK")
else:
    print("ERROR")
