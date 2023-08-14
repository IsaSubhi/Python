class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x={}, y={}".format(self.x, self.y)

    def sum_coordinates(self):
        return self.x + self.y


class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def __repr__(self):
        return "Point3D(x={}, y={}, z={}".format(
            self.x, self.y, self.z)

    def sum_coordinates(self):
        # return self.x + self.y + self.z
        return Point.sum_coordinates(self) + self.z


