# multiple_inheritance
class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name of the employee is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance form name is {self.dance}")

class Person(Dancer,Employee):
    def __init__(self,name,dance):
            self.name=name
            self.dance=dance

o=Person("Prapti", "Contemporary")
print(o.name)
print(o.dance)
o.show()