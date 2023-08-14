class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x:{self.x}, y:{self.y})"

    # self + other
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # add distance method for point (allows it to return the distance from another point)
    # add a __sub__ special method


if __name__ == '__main__':
    p1 = Point(10, 20)
    print('p1:', p1)

    p2 = Point(5, 6)

    print(p1 + p2)

