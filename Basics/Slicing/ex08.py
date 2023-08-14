x = "ABCD"

print(x)
# change x so it will contain "ZBCD"

x = 'Z' + x[1:]

print(x)

#                              ZBCD
# change x so it will contain "ZBYD"
# x = x[:2] + 'Y' + x[-1]
x = x[:2] + 'Y' + x[3]
print(x)

