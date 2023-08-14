import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    shapes = [
        Rectangle(10, 20),
        Circle(5),
        Rectangle(30, 40),
        Circle(33),
        Circle(100)
    ]

    for shape in shapes:
        print(shape.area())


    # find how many circle are in the
    # shapes list:
    circle_count = 0
    for shape in shapes:
        if isinstance(shape, Circle):
            circle_count += 1
    print(f"there are {circle_count} circles")

    # alternatively
    circle_count = 0
    for shape in shapes:
        circle_count += isinstance(shape, Circle)
    print(f"there are {circle_count} circles")


    # create a "circles" list which will contain
    # all the circles in shapes
    circles = []
    for sh in shapes:
        if isinstance(sh, Circle):
            circles.append(sh)

    print("only circles:", circles)
