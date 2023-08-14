print("PROGRAM BEGIN")

MAX = 1000


def main():
    print("bbb")

    # main:
    x = 5000
    print("main:", x)  # 5
    f()                # 7
    print("main:", x)  # 5
    g()                # 5
    print("main:", x)  # 5


def f():
    x = 5000
    print("f:", x)
    g()

def g():
    print("g:", x)


main()

print("PROGRAM END")