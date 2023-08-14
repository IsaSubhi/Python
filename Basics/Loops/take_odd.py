
numbers = [100, 123, 35, 56, 55, 78, 77]


odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("all:", numbers)
print("odd:", odd_numbers)

