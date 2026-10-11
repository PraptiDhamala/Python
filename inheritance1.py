class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def manage(self):
        print(f"{self.name} manages a team")


class Developer(Employee):
    def code(self):
        print(f"{self.name} writes code")


class Tester(Employee):
    def test(self):
        print(f"{self.name} tests software")


m = Manager("Sita", 90000)
d = Developer("Ram", 70000)
t = Tester("Hari", 60000)

m.show(); m.manage()
d.show(); d.code()
t.show(); t.test()