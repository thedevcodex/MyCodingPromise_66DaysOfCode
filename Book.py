#Make a class Book with title and author, and a method displayInfo() that prints both.
class Book():
    def __init__(self,t,a):
        self.title=t
        self.author=a
    def displayinfo(self):
        print("Book Details")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
b1=Book("Atomic Habits","Unknown")
b2=Book("Rich Dad Poor Dad","Unknown")
b1.displayinfo()
b2.displayinfo()
