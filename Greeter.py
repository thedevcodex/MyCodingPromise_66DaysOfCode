class Greeter():
    def greet(self,name=None):
        if name is None:
            print("Hello")
        else:
            print(f"Hello,{name}")
g1=Greeter()
g1.greet("alice")
