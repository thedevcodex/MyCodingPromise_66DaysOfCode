#Create a class Movie that initializes its attributes (title, rating, year) using a constructor.
class Movie():
    def __init__(self,t,r,y):
        self.title=t
        self.rating=r
        self.year=y
    def display(self):
        print("Movie Details")
        print(f"Movie Name: {self.title}")
        print(f"Movie Rating: {self.rating}")
        print(f"Movie Realese Year: {self.year}")
m1=Movie("12th Fail",9.5,2020)
m1.display()
