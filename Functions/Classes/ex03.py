class A:
    def f(self):
        print("f() of A")

    def g(self):
        print("g() of A")


class B(A):
    def g(self):
        print("g() of B")

    def h(self):
        print("h() of B")
        print("calling f method:")
        self.f()


if __name__ == '__main__':
    b1 = B()
    b1.h()

    print("---")
    b1.f()

    print("---")
    b1.g()

    print("---")
    list1 = [A(), B(), A()]
    for obj in list1:
        obj.f()

    print("---")
    for obj in list1:
        obj.g()
