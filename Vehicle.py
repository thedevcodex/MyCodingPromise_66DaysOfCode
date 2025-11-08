#Create a class Vehicle → subclass Car → subclass ElectricCar. Each should have its own displayInfo() method.
class Vehicle():
    def display_info(self):
        print("Normal Vehicle")
class Car(Vehicle):
    def display_info(self):
        super().display_info()
        print("This is Car")
class ElectricCar(Car):
    def display_info(self):
        super().display_info()
        print("This is E-Vehicle")
ev=ElectricCar()
ev.display_info()
