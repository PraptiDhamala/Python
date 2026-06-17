class Employee:
    company_name="google"
    def __init__(self,name):
        self.name=name
        self.roll=3
    def showdetails(self):
        print(f"The name of the employee is {self.name} and roll is {self.roll} and works in the company {self.company_name} ")

emp1=Employee("Harry")
emp1.roll=32
emp1.company_name="IIT"
emp1.showdetails()
# Employee.showdetails(emp1)
print(Employee.company_name)
emp2=Employee("Prapti")
emp2.roll=13
emp2.company_name="Cedar gate"
emp2.showdetails()