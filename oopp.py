class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Pranjal", 17)
student2 = Student("Prakriti", 21)

student1.display()
student2.display()