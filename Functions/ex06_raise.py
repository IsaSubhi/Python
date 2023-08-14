def divide(a, b):
    if type(a) is not int:
        raise TypeError("a must be an int")

    if type(b) is not int:
        raise TypeError("b must be an int")

    if b == 0:
        raise ValueError("b cannot be zero.")

    return a // b


def main():
    divide("asd", 5)

    a = int(input("a:"))
    b = int(input("b:"))
    result = divide(a, b)
    print(f"{a} / {b} = {result}")


if __name__ == '__main__':
    main()
