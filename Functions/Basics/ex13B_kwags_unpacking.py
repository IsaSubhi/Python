def f(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print("---")


tests = [
    {'a': 10, 'b': 20, 'c': 30},
    {'a': 10000, 'b': 200000, 'c': 300000},
    {'a': 0, 'b': 0, 'c': 0},
    {'a': -5, 'b': 0, 'c': 0},
]

for i, test in enumerate(tests, start = 1):
    print(f"TEST #{i}:")
    f(**test)
    print()



