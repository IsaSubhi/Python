# try to comment out lines 5
# or line 6 and see the results

def f():
    print(x) # error
    x = 10
    print(x)

# def f():
#     global x
#     print(x)
#     x = 10
#     print(x)


# main:
x = 1000
print(x)
f()
print(x)


