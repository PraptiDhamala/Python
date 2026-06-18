class Employee:
    company='Tesla'
    def show(self):
        print(f"The name is {self.name} and the company {self.gender} works at is {self.company}")
    @classmethod
    def changecompany(cls, newcompany):
        cls.company=newcompany

e1=Employee()
e1.name="Prapti"
e1.gender='she'
e1.show()
e1.changecompany("Google")
e1.show()
print(Employee.company)