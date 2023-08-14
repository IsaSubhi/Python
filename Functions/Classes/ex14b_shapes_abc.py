import math
from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass


class ClosedShape(Shape):
    @abstractmethod
    def area(self):
        pass


# ...

class Rectangle(ClosedShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # def area(self):
    #     return self.width * self.height
    #
    # def perimeter(self):
    #     return 2 * (self.width + self.height)


class Circle(ClosedShape):
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    # sh1 = Shape()
    # rect1 = Rectangle(10, 20)
    circ1 = Circle(11)