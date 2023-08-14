x = [10, 20, 30]

print("id of x:", id(x))

x.reverse()
print("id of x:", id(x))

x = x[::-1]
print("id of x:", id(x))