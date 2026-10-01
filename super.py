class Employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang

e1 = Employee("Prapti", 98)
e2 = Programmer("Prajoshna", 87, "Python")
print(e1.name)
print(e1.id)
print(e2.lang)
print(e2.name)
print(e2.id)
