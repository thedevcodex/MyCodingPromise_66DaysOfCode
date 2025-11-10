#Create a class Printer that prints different types of data (int, float, String) using method overloading.
class Printer():
    def print_data(self,data):
        if isinstance (data,int):
            print("Integer",data)
        elif isinstance(data,str):
            print("String",data)
        elif isinstance("Float",float):
            print('Float:',data)
p=Printer()
p.print_data(2)
p.print_data(2.5)
p.print_data("Hello")
