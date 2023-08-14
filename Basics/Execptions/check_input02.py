num = input("enter an integer:").strip()

if num and num[0] in '01234567890-' and num[1:].isdigit():
    num = int(num)
    print("10 * ", num, "=", 10*num)
else:
    print("error: not an positive integer")

print("end of program")
