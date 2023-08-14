# "/" -> parameters before this
# are positional only
def f(a, b, c, /):
    print('a:', a)
    print('b:', b)
    print('c:', c)

# f(a=10, b=20, c=30)
f(10,20,30)




