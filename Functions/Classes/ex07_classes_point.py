
class Point:
    # constructor - method
    def __init__(self):
        self.x = 100
        self.y = 200



if __name__ == '__main__':
    p1 = Point()
    print(p1.x)
    print(p1.y)
    # print(p1.z)
    p1.z = 300
    print(p1.z)

    del p1.x
    print(p1.x)

