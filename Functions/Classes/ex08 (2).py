class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x = {self.x}, y = {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Point + Point
    # Point + int
    # Point + float
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    # other + self    ---> self + other
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # other should be an int
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

class T:
    def f(self):
        pass

if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point( 5,  6)

    p3 = p1 + p2
    # p3 = p1.__add__(p2)
    # p3 = Point.__add__(p1, p2)


    t1 = T()
    # this ..
    t1.f()
    # .. is the same as:
    T.f(t1)

    p1 += 5

    print(p1)

