#Write a class Mobile that has a default constructor and a parameterized constructor.
class Mobile():
    def __init__(self,b="Unknown",p=0):
        self.brand=b
        self.price=p
    def display(self):
        print("Phone Details")
        print(f"Brand:{self.brand}")
        print(f"Price:{self.price}")
        print("------------------------")

m1=Mobile()
m1.display() #its displays default value we give unknown and 0
m2=Mobile("Realme 12x",15000) #This gives parameter we give
m2.display()
