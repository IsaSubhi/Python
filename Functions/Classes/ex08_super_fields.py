class Root:
    def __init__(self, **kwargs):
        print("init Root")


class A1(Root):
    def __init__(self, a1, **kwargs):
        print("init A1")
        self.a1 = a1
        super().__init__(**kwargs)


class A2(Root):
    def __init__(self, a2, **kwargs):
        print("init A2")
        self.a2 = a2
        super().__init__(**kwargs)


class B1(A1):
    def __init__(self, b1, **kwargs):
        print("init B1")
        self.b1 = b1
        super().__init__(**kwargs)


class B2(A2):
    def __init__(self, b2, **kwargs):
        print("init B2")
        self.b2 = b2
        super().__init__(**kwargs)


class C(B1, B2):
    def __init__(self, c, **kwargs):
        print("init C")
        self.c = c
        super().__init__(**kwargs)


if __name__ == '__main__':
    c = C(a1=10, a2=20, b1=30, b2=40, c=50)


    