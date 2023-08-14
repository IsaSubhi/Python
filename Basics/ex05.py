countries = [
    'israel',
    'russia',
    'japan',
    'norway',
    'china',
    'narnia',
    'india',
    'turkey',
    'north korea',
]

print('narnia' in countries)
print(countries)
print()

countries.remove('narnia')

print('narnia' in countries)
print(countries)
print()


countries.reverse()
print("after reverse:")
print(countries)
print()

# countries = countries[::-1]
countries.reverse()
print("after [::-1]:")
print(countries)
print()

