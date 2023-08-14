def f(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)

# positional argument
f(10, 20, 30)

# keyword argument
f(c=111, a=23, b=45)


f(10, b=20, c=30)
f(10, c=20, b=30)
print("----")
f(10, a=20, b=30) # illegal

