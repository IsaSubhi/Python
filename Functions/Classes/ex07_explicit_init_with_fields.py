class A1:

    def __init__(self, a1):
        print("init A1")
        self.a1 = a1

    def f(self):
        print("f() of A1")


class A2:
    def __init__(self, a2):
        print("init A2")
        self.a2 = a2

    def f(self):
        print("f() of A2")


class B1(A1):
    def __init__(self, a1, b1):
        print("init B1")

        print("explicit call to A1 init")
        A1.__init__(self, a1)

        self.b1 = b1



class B2(A2):
    def __init__(self, a2, b2):
        print("init B2")

        print("explicit call to A2 init")
        A2.__init__(self, a2)

        self.b2 = b2



class C(B1, B2):
    def __init__(self, a1, b1, a2, b2, c):
        print("init C")

        print("explicit call to B1 init")
        B1.__init__(self, a1, b1)

        print("explicit call to B2 init")
        B2.__init__(self, a2, b2)

        self.c = c


if __name__ == '__main__':
    c = C(1, 2, 3, 4, 5)

    