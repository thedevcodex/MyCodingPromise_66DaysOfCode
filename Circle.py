#Create a class Circle with a constructor that accepts radius and a method to calculate area and circumference.
import math
class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        formula=math.pi*(self.radius**2)
        return formula
    def circumference(self):
        return 2*math.pi*self.radius
a=Circle(5)
print(f"Area:,{a.area():.2f}")


c=Circle(4)
print(f"Circumference:{c.circumference():.2f}")
