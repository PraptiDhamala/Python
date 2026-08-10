class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
student1 = Student("Prapti", 20)
student2 = Student("Anusha", 21)

student1.display()
student2.display()