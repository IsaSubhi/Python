def f(a,b,c):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print("---")

x = 10,20,30
f(*x)

y = {'c' : 1, 'b': 2, 'a': 3}
f(a=y['a'], b=y['b'], c=y['c'])
f(**y)         # a=3, b=2, c=1
f(*y.values()) # a=1 b=2 c=3


