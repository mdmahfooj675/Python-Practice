# Create a class Rectangle.
# - Create two objects: r1 and r2.
# - Assign length and width to each object.
# - Calculate and print the area of both rectangles.
# Formula: Area = length × width.

class Rectangle:
    def __init__(self , length , weidth):
        self.length = length
        self.weidth = weidth

    def display(self):
        return self.length*self.weidth

R1 = Rectangle(2 , 3)
print("length of the rectangle : " , R1.length)
print("weidth of the rectangle : " , R1.weidth)
print("area of the rectangle :  " , R1.display())

print("--------------------------------------")

R2 = Rectangle(5.4 , 8.7)
print("length of the rectangle : " , R2.length)
print("weidth of the rectangle : " , R2.weidth)
print("area of the rectangle :  " , R2.display())