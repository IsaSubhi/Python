# Encapsulation
# class Point:
#
#     def __init__(self, x, y):
#         self.__x=x
#         self.__y=y
#         self.__number=1
#
#     # def getter(self):
#     #     return self.__x, self.__y
#     #
#     # def setter(self, value1, value2):
#     #     self.__x=value1
#     #     self.__y=value2
#
#     def getter2(self):
#         return self.__number


# point1=Point(3, 7)
# # print("X is: {}, Y is:{}".format(*point1.getter()))
# # point1.setter(2, 6)
# # print("X is: {}, Y is:{}".format(*point1.getter()))
# print("This is point number {}.".format(point1.getter2()))

# Absrtraction
# class Point:
#
#     def __init__(self, x, y):
#         self.__x=x
#         self.__y=y
#
#     def point_getter(self):
#         return self.__x, self.__y
#
# class Line:
#
#     def __init__(self, x1, y1, x2 ,y2):
#         self.__point1=Point(x1, y1)
#         self.__point2=Point(x2, y2)
#
#     def line_getter(self):
#         print("The first point is: {}, {}, the second point is: {}, {}.".\
#               format(*self.__point1.point_getter(), *self.__point2.point_getter()))
#
# line1=Line(2, 3, 6, 7)
# line1.line_getter()

# Inheritance
# class Point:
#
#     def __init__(self, x, y):
#         self._x=x
#         self._y=y
#
# class Point3D(Point):
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.__z=z
#
#     def getter(self):
#         print(f"The attributes of the point are: {self._x}, {self._y}, {self.__z}.")


# point4=Point3D(5, 8, 13)
# point4.getter()

# Multiinheritance
class Class1:
    def m(self):
        print("in Class 1.")

class Class2(Class1):
    def m(self):
        print("in Class 2.")

class Class3(Class1):
    def m(self):
        print("in Class 3.")

class Class4(Class2, Class3):
    pass

Class4.m(Class4)
# Class3.m(Class3)
# Class1.m(Class2)
# Class1.m(Class4)
# Class3.m(Class4)