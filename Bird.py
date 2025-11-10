#Create a parent class Bird with a method fly(). Override it in classes Eagle and Parrot.
class Bird():
    def fly(self):
        print('Bird Fly')
class Eagle(Bird):
    def fly(self):
        print("Eagle fils Higher")
class Parrot(Bird):
    def fly(self):
        print("Parrot Files")
b1=Bird()
e1=Eagle()
p1=Parrot()

for bird in (b1,e1,p1):
    bird.fly()
