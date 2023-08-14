num = int(input("enter an int:"))

if num % 2 == 0:
    print("is even")
else:
    print("is odd")


if num % 2 == 0:
    status = "even"
else:
    status = "odd"

print(f"is {status}")
# print("is {}".format(status))

# other languages:
# status = CONDITION ? VALUE1 : VALUE2
# in python:
# status = VALUE1 if CONDITION else VALUE2

status = "even" if num % 2 == 0 else "odd"
print(f"is {status}")

print(f"is {'even' if num % 2 == 0 else 'odd'}")





