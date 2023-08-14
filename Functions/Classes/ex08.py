
class Point:
    # constructor - method
    def __init__(self):
        print(f"initializing point {id(self)}...")
        self.x = 100
        self.y = 200


    def show(self):
        print(f"(x:{self.x}, y:{self.y})")

    def __del__(self):
        print(f"point object {id(self)} deleted")


if __name__ == '__main__':
    p1 = Point()
    p1.show()
    p1.x = 500
    p1.show()
