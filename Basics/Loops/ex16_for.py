names = ['david', 'moshe', 'shlomo', 'sarah', 'lea']
#           0       1        2         3        4
for name in names:
    print(name)

print("-- in reverse --")

for name in names[::-1]:
    print(name)


print("-- even positions only (second, fourth ...) --")

#           ['moshe','sarah']
for name in names[1::2]:
    print(name)
