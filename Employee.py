#Create a class Employee with a constructor to initialize name and salary, then display the details.
class Employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    def display(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")
e1=Employee("Sam",80000)
e1.display()
