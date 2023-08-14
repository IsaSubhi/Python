x = [10, 20, 30]
y = x  # y is now an alias of the same object x point to

print(id(x), "x:", x)
print(id(y), "y:", y)
print()

x.reverse()
print("after x.reverse()")
print(id(x), "x:", x)
print(id(y), "y:", y)
print()

x = x[::-1]
print("after x[::-1]")
print(id(x), "x:", x)
print(id(y), "y:", y)
print()
