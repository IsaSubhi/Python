num = input("enter an integer:")

if num.isdigit():
    num = int(num)
    print("10 * ", num, "=", 10*num)
else:
    print("error: not an positive integer")

print("end of program")