class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x = {self.x}, y = {self.y}'


class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def __repr__(self):
        return Point.__repr__(self) + f', z = {self.z}'


def main():
    p1 = Point(10, 20)
    print('p1 = ', p1)

    p2 = Point3D(11, 22, 33)
    print('p2 = ', p2)

    print("isinstance(p1, Point) = ", isinstance(p1, Point))
    print("isinstance(p2, Point) = ", isinstance(p2, Point))

    print("type(p1) is Point = ", type(p1) is Point)
    print("type(p2) is Point = ", type(p2) is Point)


if __name__ == '__main__':
    main()
