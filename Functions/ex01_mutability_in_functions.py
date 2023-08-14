numbers = [10, 20, 30]

def add_one(numbers):
    print("add one:")
    print("numbers id:", id(numbers))

    for i in range(len(numbers)):
        numbers[i] += 1

    print("add one END")


def change(numbers):
    print("change:")
    print("numbers id before change:", id(numbers))
    numbers = [123, 456, 789]
    print("numbers id after change:", id(numbers))
    print("change END")


print("numbers id: ", id(numbers))
print(numbers)
add_one(numbers)
print(numbers)
change(numbers)
print(numbers)
