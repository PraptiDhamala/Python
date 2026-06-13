class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetail(self):
        print(f"The name of Employee:{self.id} is {self.name}")
class Programmer(Employee):
    def showlanguage(self):
        print("The default language is py")
e1= Employee("Pranjalliiiiiiiii",10009)
e1.showdetail()
e2= Programmer("Prakritiiiii",9088)
e2.showdetail()
