def f(*args):
    print(args)
    for argument in args:
        print(argument)


f(1, 2, 3, 4)
print("-----------------")

# keyword arguments
def f2(**kwargs):
    print(kwargs)


f2(a=1,apple=2,x=3,abc=4)
print("-----------------")

def f3(*args, **kwargs):
    print(args)
    print(kwargs)


f3()
f3(1,2,3, a=10,b=20)
print("-------")

def f4(a,b,c, *args):
    print("a:",a,"b:", b,"c:", c)
    print(args)


f4(a=10, b=20, c=30)
f4(10, 20, 30, 40, 50, 60)

def f5(a,b,c, *args, x, y, z, **kwargs):
    print("a:",a,"b:", b,"c:", c)
    print("x:",x,"y:", y,"z:", z)
    print(args)
    print(kwargs)

f5(1,2,3,4,5,6,7,8,9,10,x=11,y=22,z=33)
print("------")

def f6(a, b, c, *, x, y, z):
    print("a:", a, "b:", b, "c:", c)
    print("x:", x, "y:", y, "z:", z)

f6(1,2,3,4,5,6)
