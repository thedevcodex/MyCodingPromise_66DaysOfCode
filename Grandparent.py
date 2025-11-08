#Demonstrate multilevel inheritance using Grandparent → Parent → Child.
class Grandparent():
    def __init__(self,gn):
        self.grandparent_name=gn
    def show_name(self):
        print("Grandparent Name:",self.grandparent_name)
class Parent(Grandparent):
    def __init__(self,gn,pn):
        super().__init__(gn)
        self.parentname=pn
    def show_name2(self):
        super().show_name()
        print("Parent Name:",self.parentname)
class child(Parent):
    def __init__(self,gn,pn,cn):
        super().__init__(gn,pn)
        self.child_name=cn
    def show_name3(self):
        super().show_name2()
        print("Child Name:",self.child_name)

obj=child("David","Bravis","Sarvesh")
obj.show_name3()

