import math


class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
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
    circle_count = len([sh for sh in shapes if isinstance(sh, Circle)])
    print(f"there are {circle_count} circles")

    # create a "circles" list which will contain
    # all the circles in shapes
    circles = [sh for sh in shapes if isinstance(sh, Circle)]
    print("only circles:", circles)


    # find the area of the circle with the largest area
    print(
        "max circle area:",
        max(sh.area() for sh in shapes if isinstance(sh, Circle))
    )

    # does "shapes" contain any circles?
    # classic:
    has_any_circle = False
    for sh in shapes:
        if isinstance(sh, Circle):
            has_any_circle = True
            break
    print("shapes {} circles".format('has' if has_any_circle else 'has no'))

    # comprehension:
    print("does shapes has any circles?")
    print(any(isinstance(sh, Circle) for sh in shapes))
    


