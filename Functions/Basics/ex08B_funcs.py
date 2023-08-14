def average(*numbers):
    # print("type of numbers:", type(numbers))
    # print("numbers:", numbers)

    if len(numbers) < 1:
        result = 0
    else:
        result = sum(numbers) / len(numbers)

    return result


print(average(10, 20, 30))
print(average(10000, 222, 31, 4444))
print(average())

x = [100, 201, 305]
print(average(x[0], x[1], x[2]))
print(average(*x))
print("~~~~~")
print(x)
print(*x)
print(x[0], x[1], x[2])
