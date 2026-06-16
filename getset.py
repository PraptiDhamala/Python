class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):          # Getter
        return self._name

    @name.setter
    def name(self, value):   # Setter
        self._name = value

s = Student("Ram")

print(s.name)   # Calls getter

s.name = "Hari" # Calls setter

print(s.name)