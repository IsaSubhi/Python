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
        result = Point(self.x, self.y)
        result += other
        return result

    # other + self    ---> self + other
    def __radd__(self, other):
        return self + other

    # self += other
    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        else:
            return NotImplemented

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
    print(f"id: {id(p1)}, value: {p1}")
    p1 += 5
    # --> p1 = p1 + 5 (the addition creates a new object)
    print(f"id: {id(p1)}, value: {p1}")

