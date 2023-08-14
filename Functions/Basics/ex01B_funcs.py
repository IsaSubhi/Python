print("PROGRAM BEGIN")

def f():
    x = 5000
    print("f:", x)

f()
print("aaaa")
# g() # runtime error

def g():
    print("g:", x)


print("bbb")

# main:
x = 5000
print("main:", x)  # 5
f()                # 7
print("main:", x)  # 5
g()                # 5
print("main:", x)  # 5

print("PROGRAM END")