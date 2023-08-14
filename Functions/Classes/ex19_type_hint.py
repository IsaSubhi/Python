
class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(12)
    p3 = Point(13, 14)
    p33 = Point("123", 2.5)


