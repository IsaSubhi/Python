

def f1(x, y, z):
    print("f1:")
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("------")


f1(1, 2, 3)
# f1(1, 2)
# f1(1, 2, 3, 4)
f1(x=10, y=20, z=30)
f1(z=10, y=20, x=30)
f1(100, z=5, y=6)

def f2(x, y=222, z=333):
    print("f2:")
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("------")

f2(1, 2, 3)
f2(1, 2)
f2(1)
# f2()
# f2(1,2,3,4)
