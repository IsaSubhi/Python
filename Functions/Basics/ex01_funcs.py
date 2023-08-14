def f():
    x = 5000
    print("f:", x)


def g():
    print("g:", x)


# main:
x = 5000
print("main:", x)  # 5
f()                # 7
print("main:", x)  # 5
g()                # 5
print("main:", x)  # 5
