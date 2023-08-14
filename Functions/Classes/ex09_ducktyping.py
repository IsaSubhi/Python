class A:
    def f(self):
        print("f of A")

class B:
    def f(self):
        print("f of B")

class C:
    def f(self):
        print("f of C")

class D:
    def __init__(self, f):
        self.f = f

if __name__ == '__main__':
    list1 = [
        A(), B(), A(), C(),
        # 10,
        # D(111),
        B(), A()
    ]

    for obj in list1:
        obj.f()
