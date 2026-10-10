class Animal:
    def speak(self):
        print("Some generic animal sound.")

    def eat(self):
        print("This animal eats food.")

class Mammal(Animal):
    def speak(self):  # overrides Animal.speak
        print("Mammal makes a sound.")

class Dog(Mammal):
    def speak(self):  # overrides Mammal.speak
        print("Dog barks: Woof!")

    def eat(self):  # overrides Animal.eat
        super().eat()  # still calls the parent version
        print("The dog eats bones.")

a = Animal()
m = Mammal()
d = Dog()

a.speak()
m.speak()
d.speak()
d.eat()