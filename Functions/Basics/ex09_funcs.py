def f(a, b, c, *args): #, d, e, f):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
    # print('d:', d)
    # print('e:', e)
    # print('f', f)
    print()

f(10, 20, 30)
f(10, 20,30,40,50)
f(a=40,b=50, c=60)
f(40,b=50, c=60)
f(40, 50, c=60)
f(a=40,b=50, c=60)



