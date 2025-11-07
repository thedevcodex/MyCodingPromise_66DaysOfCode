#Create a class Temperature with a method to convert Celsius to Fahrenheit.
class Temperature():
    def __init__(self,t):
        self.celsius=t
    def display(self):
        f=(self.celsius*9/5)+32
        print(f"{self.celsius}°C = {f}°F")
temp_c=Temperature(100)
temp_c.display()
