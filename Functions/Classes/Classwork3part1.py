class Rectangle:
    # field. It belongs to each of rectangles
    amount=0
    def __init__(self, side1, side2):
#       attributes of specific rectangle
        self.r_side1=side1
        self.r_side2=side2
        Rectangle.amount+=1

    def show_sides(self):
        print("The first side:", self.r_side1)
        print("The second side:", self.r_side2)

    def __del__(self):
        Rectangle.amount-=1

if __name__=="__main__":
    rect1=Rectangle(5, 9)
    print(f"The amount of rectangles is: {Rectangle.amount}")
    print(f"The amount of rectangles is: {rect1.amount}")
    rect1.show_sides()
    rect2=Rectangle(3, 4)
    print(f"The amount of rectangles is: {Rectangle.amount}")
    print(f"The amount of rectangles is: {rect1.amount}")
    print(f"The amount of rectangles is: {rect2.amount}")
    rect2.show_sides()
    rect2.__del__()
    del rect2
    print(f"The amount of rectangles is: {Rectangle.amount}")
    print(f"The amount of rectangles is: {rect1.amount}")
    print(f"The amount of rectangles is: {rect2.amount}")