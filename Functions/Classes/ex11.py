
class Point:
    # "static" variable / class variable
    # exists only once for the class itself (not its instances)
    count = 0

    # constructor - method
    def __init__(self):
        # print(f"initializing point {id(self)}...")

        Point.count += 1
        # self.count += 1 # can use instance but not recommended

        self.x = 100
        self.y = 200

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")

    # python calls this function automatically
    # before the object is deleted from memory
    def __del__(self):
        # print(f"point object {id(self)} deleted")
        Point.count -= 1

if __name__ == '__main__':
    p1 = Point()
    p1.x = 10
    p1.y = 20

    print(f"there are {Point.count} points in memory")

    p2 = Point()
    p2.x = 111
    p2.y = 222

    print(f"there are {Point.count} points in memory")

    del p1
    print(f"there are {Point.count} points in memory")

    p3 = p2
    print(f"there are {Point.count} points in memory")

    del p2
    print(f"there are {Point.count} points in memory")

    del p3
    print(f"there are {Point.count} points in memory")

    points = [Point(), Point(), Point(), Point()]
    print(f"there are {Point.count} points in memory")

    del points[2:]

    print(f"there are {Point.count} points in memory")

