#Write a class Student with name and marks. Create 3 student objects and display their info.
class Student():
    def __init__(self,n,m):
        self.name=n
        self.mark=m
    def details(self):
        print(f"Student Name:{self.name}")
        print(f"Marks:{self.mark}")
s1=Student("Sam",89)
s2=Student("Thashleema",90)
s1.details()
s2.details()
