def my_decorator(func1):
    def inner():
        func1()
        print("Done! What to do next?")
    return inner()


@my_decorator
def multiplcation():
    first_number=int(input("Enter the first integer number: "))
    second_number=int(input("Enter the second integer number: "))
    print(f"The result of {first_number} * {second_number} is: {first_number*second_number}")

@my_decorator
def division():
    print("15/3={}".format(15/3))