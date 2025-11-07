#Create a class Rectangle that takes length and width and has a method area() to calculate the area.
class Rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print(f"Area Of the Rectangle: {self.length*self.breadth}")
l=int(input("Enter Length:"))
b=int(input("Enter breadth:"))
a=Rectangle(l,b)
a.area()
