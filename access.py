class employee:
    def __init__(self):
        self.name="Papu"
a=employee()
print(a.name)  
# public

class employee:
    def __init__(self):
        self.__name="Papu"
a=employee()
# print(a.__name)  
print(a._employee__name) #name mangaling:used to protect class private and superclass private attributes from being overriden
# _classname__attribute
# private


# chaina access modifier just manche haru le convention use garna
