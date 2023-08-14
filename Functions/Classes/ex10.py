
class Point:
    # constructor - method
    def __init__(self):
        print(f"initializing point {id(self)}...")
        self.x = 100
        self.y = 200

    def show(self):
        print(f"(x:{self.x}, y:{self.y})")

    # python calls this function automatically
    # before the object is deleted from memory
    def __del__(self):
        print(f"point object {id(self)} deleted")


def f():
    p3 = Point()
    p3.x = 800
    p3.y = 900
    p3.show()


if __name__ == '__main__':

    print("creating a point without a variable")
    print("and calling show on it")

    Point().show()

    open("1.txt", "w").write("Hello")


    print("p1 = Point()")
    p1 = Point()

    print("p1.x = 500")
    p1.x = 500

    print("calling f()")
    f()
    print("returned from f()")

    print("p2 = p1")
    p2 = p1

    print("deleting p1")
    del p1

    # print("deleting p2")
    # del p2

    print("end of program")



