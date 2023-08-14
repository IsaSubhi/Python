
# import math
#
# def f():
#     print(math.pi)


# usually you do not want to write code like this
# (it can be useful in cases the module is slow to
#  load and is only used rarely)
def f():
    import math
    print(math.pi)


