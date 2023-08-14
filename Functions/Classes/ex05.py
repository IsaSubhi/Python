class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x = {self.x}, y = {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


    def __add__(self, other):
        if type(other) in (int, float):
            return Point(self.x + other, self.y + other)
        elif type(other) is Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("other should be a Point, int, or float")


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # other should be an int
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)



if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = p1 + 1000
    p3 = p1 + p2
    print(p1, p2, p3)