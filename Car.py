#Create a class Car with attributes brand, model, and year. Create two objects and print their details. 
class Car():
    def __init__(self,b,m,y):
        self.brand=b
        self.model=m
        self.year=y
    def display(self):
        print("Car Details")
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
c1=Car("Audi","xy2",2020)
c2=Car("BMW","hyt7",2023)
c1.display()
c2.display()
