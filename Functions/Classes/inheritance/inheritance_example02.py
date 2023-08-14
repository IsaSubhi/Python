# warning: super() might not work as expected with mutiple inheritance
#
# for more information about using super in classes:
#
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

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
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return "Point3D(x={}, y={}, z={}".format(
            self.x, self.y, self.z)

    def sum_coordinates(self):
        # return self.x + self.y + self.z
        return super().sum_coordinates() + self.z


