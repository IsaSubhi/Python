x = 1000
y = 2000
print("X =", x, end=' ')
print("Y =", y)

t = x
x = y
y = t

print("X =", x, end=' ')
print("Y =", y)

x, y = y, x

print("X =", x, end=' ')
print("Y =", y)


