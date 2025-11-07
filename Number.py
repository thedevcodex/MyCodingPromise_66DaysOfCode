#Create a class Number that checks if a number is even or odd using a method.
class Number():
    def __init__(self,num):
        self.num=num
    def check(self):
        res=self.num
        if res%2==0:
            print(f"{res} is Even")
        else:
            print(f"{res} is Odd")
n1=Number(10)
n1.check()
