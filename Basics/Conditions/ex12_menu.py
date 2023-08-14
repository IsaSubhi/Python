
print("1) Orange Juice")
print("2) Cola")
print("3) Ice Tea")

drink_number = int(input("enter drink number:"))

if drink_number == 1:
    drink_name = "Orange Juice"
elif drink_number == 2:
    drink_name = "Cola"
elif drink_number == 3:
    drink_name = "Ice Tea"
else:
    drink_name = "No such drink"

print("You got", drink_name)
