
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(12)
    p3 = Point(13,14)

    p1.show()
    p2.show()
    p3.show()

