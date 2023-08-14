def f():
    global x

    print("f begin")
    print("f before:", x)
    x = 9999
    print("f after:", x)
    if x > 100:
        x = 100_000

    print("f end")


def g():
    x = 7000
    print("g:", x)


def h():
    print("h:", x)



# main:
x = 1000
print("main:", x)
f()
print("main:", x) # <--- ???
g()
print("main:", x)
