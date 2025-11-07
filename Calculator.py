#Create a Calculator class with methods add(), subtract(), multiply(), and divide().Overload add() method to add:Two integersThree integers
class Calculator():
    def add(self,a,b,c=None):
        if c is None:
            print("Add:",a+b)
        else:
            print("Add:",a+b+c)
    def subract(self,a,b):
        print("Subract:",a-b)
    def multiply(self,a,b):
        print("Multiply:",a*b)
    def division(self,a,b):
        if b!=0:
            print("Division:",a/b)
        else:
            print("error cannot divide By zero")
calc=Calculator()
calc.add(10,5)
calc.add(10,5,5)
calc.subract(10,5)
calc.multiply(10,2)
calc.division(10,2)
calc.division(10,0)
