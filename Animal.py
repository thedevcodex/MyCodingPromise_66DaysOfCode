#Create a class Animal with a method sound(). Derive classes Dog and Cat and override the sound.
class Animal():
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Meow")
d1=Dog()
d1.sound()
c1=Cat()
c1.sound()
