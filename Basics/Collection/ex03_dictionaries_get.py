x = {
    'david': 100,
    'moshe': 90,
    'shlomo': 80
}

name = input("enter name:")

# print(f'{name} --> {x[name]}')
# print(x[name])
# print(x.get(name)) # can return None
print(x.get(name, 'No such name'))


