class Shape():
    def area(self):
        print("Area")
class Square():
    def area(self,a):
        print("Area of the Square:",a**2)
class Rectangle():
    def area(self,l,w):
        print("Area of Rectangle:",l*w)
class Triangle():
    def area(self,b,h):
        print("Area of Triangle:",0.5*b*h)

s1=Shape()
s1.area()
S1=Square()
S1.area(2)
r1=Rectangle()
r1.area(2,3)
t1=Triangle()
t1.area(3,4)
