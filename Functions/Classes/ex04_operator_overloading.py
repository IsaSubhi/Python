class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x = {self.x}, y = {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


    def __add__(self, other):
        # new_x = self.x + other.x
        # new_y = self.y + other.y
        # new_point = Point(new_x, new_y)
        # return new_point

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # other should be an int
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

