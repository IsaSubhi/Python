
class Point:
    def __init__(self, x=0, y=0):
        x = int(x)
        y = int(y)

        self.x = x
        self.y = y

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(12)
    p3 = Point(13, 14)
    p33 = Point("123", 2.5)
    p33.show()
    # Point.show(self = p33)

    p4 = Point("Hello", "World")

