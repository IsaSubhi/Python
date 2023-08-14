
class Point:
    # "static" variable / class variable
    # exists only once for the class itself (not its instances)
    count = 0

    # constructor - method
    def __init__(self):
        Point.count += 1
        print(f"INIT: there are {Point.count} points in memory")

        self.x = 100
        self.y = 200

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")

    # python calls this function automatically
    # before the object is deleted from memory
    def __del__(self):
        Point.count -= 1
        print(f"DEL : there are {Point.count} points in memory")

if __name__ == '__main__':
    p1 = Point()
    p1.x = 10
    p1.y = 20

    p2 = Point()
    p2.x = 111
    p2.y = 222

    del p1


    p3 = p2

    del p2

    del p3

    points = [Point(), Point(), Point(), Point()]

    del points[2:]


