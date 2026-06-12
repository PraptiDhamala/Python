class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetail(self):
        print(f"The name of Employee:{self.id} is {self.name}")

e1= Employee("Pranjalliiiiiiiii",10009)
e1.showdetail()
e2= Employee("Prakritiiiii",9088)
e2.showdetail()
