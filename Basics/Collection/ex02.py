x = []
print(x)
x.append(10)
print(x)
x.append(20)
print(x)
print(x[0])
print(x[1])
print(x[-1])

print(x[0] * x[1])

x.append(30)
x.append(40)
print(x)

print(x[1:-1])
print(x)
print(x[::-1])
print(x[::-2])
print(x[0::-2])

print("-----------")
print(x)
y = x.pop()
print(y)
print(x)
y = x.pop(1)
print(y)
print(x)
