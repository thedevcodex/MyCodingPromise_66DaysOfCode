#overload constructors in a Box class to initialize:only side, and length, breadth, height.
class box():
    def __init__(self,l=None,b=None,h=None):
        if  b is None and h is None:
            self.l=self.b=self.h=l
            print("This is Cube")
        else:
            self.l=l
            self.b=b
            self.h=h
            print("This is box")
    def volume(self):
        ans=self.l*self.b*self.h
        print("volume:",ans)
b1=box(5)
b1.volume()
b2=box(2,3,4)
b2.volume()
        
