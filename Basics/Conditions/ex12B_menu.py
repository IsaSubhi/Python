
# this example only works in python versions 3.10 and up!

print("1) Orange Juice")
print("2) Cola")
print("3) Ice Tea")

drink_number = int(input("enter drink number:"))

match drink_number:
    case 1:
        drink_name = "Orange Juice"
    case 2:
        drink_name = "Cola"
    case 3:
        drink_name = "Ice Tea"
    case _:
        drink_name = "No such drink"

print("You got", drink_name)
