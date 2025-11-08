#Create a class Person and a subclass Employee that adds employeeId and department.
class Person():
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class Employee(Person):
    def __init__(self,n,a,empid,d):
        super().__init__(n,a)
        self.employeeid=empid
        self.dept=d
    def display(self):
        super().show_info()
        print("Employee Id:",self.employeeid)
        print("Department:",self.dept)
emp=Employee("Sam",19,"123","CS")
emp.display()
