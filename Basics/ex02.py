name = input('Enter your name: ')

width = len(name) + 4

print('*' * width)
print('*', name, '*')
print('*' * width)


print('*' * width)
print('* ', name, ' *', sep='')
print('*' * width)
