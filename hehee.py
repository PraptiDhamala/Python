class Employee:
    company="Apple"
    def show(self):
        print(f"The employee name is {self.name} and the company is {self.company}")
    
    def changecompany(cls,newcompany):
        cls.company= newcompany

e1=Employee()
e1.name="Prajoshna"
e1.show()
e1.changecompany("Tesla")
e1.show()