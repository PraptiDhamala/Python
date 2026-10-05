class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):          # Dog inherits only from Animal
    def bark(self):
        print(f"{self.name} says Woof!")


d = Dog("Buddy")
d.eat()    # inherited from Animal -> Buddy is eating
d.bark()   # defined in Dog -> Buddy says Woof!