#Write a class Laptop with brand, ram, and price, and a method to print specs.

class Laptop():
    brand=input("Enter Brand:")
    ram=input('Enter Ram:')
    price=int(input("Enter Price:"))
    def specs(self):
        print("Laptop Specs:")
        print(f"Brand:{Laptop.brand}")
        print("Ram(GB)",Laptop.ram)
        print("Price",Laptop.price)
l1=Laptop()
l1.specs()
