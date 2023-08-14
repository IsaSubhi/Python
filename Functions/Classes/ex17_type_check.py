
class Point:
    def __init__(self, x=0, y=0):
        if type(x) is not int:
            raise TypeError("x must be an int")

        if type(y) is not int:
            raise TypeError("y must be an int")

        self.x = x
        self.y = y

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(12)
    p3 = Point(13, 14)

    p4 = Point("Hello", "World")

