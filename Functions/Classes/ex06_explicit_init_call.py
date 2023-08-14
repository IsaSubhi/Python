class A1:
    def __init__(self):
        print("init A1")

    def f(self):
        print("f() of A1")


class A2:
    def __init__(self):
        print("init A2")

    def f(self):
        print("f() of A2")


class B1(A1):
    def __init__(self):
        print("init B1")

        print("explicit call to A1 init")
        A1.__init__(self)


class B2(A2):
    def __init__(self):
        print("init B2")

        print("explicit call to A2 init")
        A2.__init__(self)


class C(B1, B2):
    def __init__(self):
        print("init C")

        print("explicit call to B1 init")
        B1.__init__(self)

        print("explicit call to B2 init")
        B2.__init__(self)



if __name__ == '__main__':
    c = C()

    