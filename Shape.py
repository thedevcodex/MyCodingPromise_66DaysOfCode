#Create a base class Shape and child classes Rectangle and Triangle with area methods.
class Shape():
    def area(self):
        print("Shape")
class Rectangle(Shape):
    def area(self,l,b):
        super().area()
        print("Area of Rectangle is:",l*b)
class Triangle(Rectangle):
    def area(self,l,b,h):
        super().area(l,b)
        print('Area of Triangle:',0.5*b*h)
r1=Rectangle()
#r1.area(2,3)
t1=Triangle()
t1.area(2,3,4)
