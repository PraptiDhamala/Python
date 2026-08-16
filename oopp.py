class Student:
    def __init__(self, name, age,address):
        self.name = name
        self.age = age
        self.address=address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


student1 = Student("Pranjal", 17,"USA")
student2 = Student("Prakriti", 21,"AUS")
student3 = Student("Prapti", 24,"UK")

student1.display()
student2.display()