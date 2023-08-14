"""
string at start of document
is a documentation of the module
"""


class Point:
    """
    this is documentation for the class
    """

    def __init__(self, x: int = 0, y: int = 0):
        """
        creates a point with x and y values

        x - an int value for x coordinate
        y - an int value for y coordinate
        """
        self.x = x
        self.y = y

    def show(self):
        """
        prints the point data on the screen
        """
        print(f"(x:{self.x}, y:{self.y})")


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(12)
    p3 = Point(13, 14)
    p33 = Point("123", 2.5)

    p1.show


