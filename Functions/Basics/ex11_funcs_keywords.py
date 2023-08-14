# "*," -> parameters after this
# are keyword only
def f(x, z, *, a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)

# f(a=10, b=20, c=30)
print("---")
f(a=10, b=20, c=30)




