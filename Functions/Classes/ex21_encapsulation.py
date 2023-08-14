class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point_a = Point(x1, y1)
        self.point_b = Point(x2, y2)


if __name__ == '__main__':
    line1 = Line(10,20,30,40)
