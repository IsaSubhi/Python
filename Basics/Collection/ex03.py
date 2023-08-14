x = [10, 20, 30, 40, 50, 60, 70]
y = x
# z = x.copy()
z = x[:]

print("x: ", x)
print("y:", y)
print("z:", z)
print()

x[3] = 777
print("id of x:", id(x))
print("x: ", x)
print("id of y:", id(y))
print("y:", y)
print("z:", z)
print(len(x))
print(x.pop())
print(len(x))

