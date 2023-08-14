def f(a, b, c, *args, d, e, f):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    print('d:', d)
    print('e:', e)
    print('f', f)
    print()

# a=10 b=20 c=30 args=() d=11 e=22 f=33
f(10, 20, 30, d=11,e=22,f=33)




