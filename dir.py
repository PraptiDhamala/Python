x=[1,2,3]
print(dir(x))

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1=Employee("Prapti",9000000)
print(e1.__dict__)