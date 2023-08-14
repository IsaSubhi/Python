x = {
    'a': [ 'apple', 'arm', 'avocado' ],
    'b': [ 'banana', 'baloon'],
    'c': ['car', 'counter']
}
print(x['a'])
print(x['c'])
# print(x['d'])

# add 'animal' to the 'a' list

# x['a'].append('animal')
x['a'].insert(0, 'animal')

print(x['a'])
# print(x[0])
# print(x[0:])

print(x['a'][0])

