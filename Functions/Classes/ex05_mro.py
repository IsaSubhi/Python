class A1:
    def __init__(self):
        print("init A1")
        super().__init__()

    def f(self):
        print("f() of A1")


class A2:
    def __init__(self):
        print("init A2")
        super().__init__()

    def f(self):
        print("f() of A2")


class B1(A1):
    def __init__(self):
        print("init B1")
        super().__init__()


class B2(A2):
    def __init__(self):
        print("init B2")
        super().__init__()


class C(B1, B2):
    def __init__(self):
        print("init C")
        super().__init__()


"""
  object
 /   \
A1   A2 
|    |
B1   B2
 \   /
   C

C -> B1 -> A1 -> B2 -> A2 -> object

"""


if __name__ == '__main__':
    c = C()
    print(C.mro())
    