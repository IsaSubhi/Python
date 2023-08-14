
numbers = [100, 123, 35, 56, 55, 78, 77]

numbers2 = [x * 10 for x in numbers if (x % 2 != 0)]

print("all:", numbers)
print("x10:", numbers2)

for number in (x * 10 for x in numbers if (x % 2 != 0)):
    print(number)
