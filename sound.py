#Demonstrate runtime polymorphism by calling overridden methods through a parent reference.
class Animal():
    def sound(self):
        print('Sound')
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat Meow")
a1=Animal()
a1.sound()

d1=Dog()
d1.sound()

c1=Cat()
c1.sound()
