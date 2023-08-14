class A1:
    def f(self):
        print("f() of A1")


class A2:
    def f(self):
        print("f() of A2")


class B(A1, A2):
    pass


if __name__ == '__main__':
    b1 = B()
    b1.f()
    print("mro of B:", B.mro())
