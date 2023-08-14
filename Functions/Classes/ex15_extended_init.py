
class Point:
    def __init__(self, x, y=None):

        if y is None:
            y = x

        self.x = x
        self.y = y

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point(y=100, x=200)
    p3 = Point(345)

    p1.show()
    p2.show()
    p3.show()

