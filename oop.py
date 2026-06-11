# # helps us to map entities ro real world entities
# class is blueprint
# objects is instance 


class person:
    name="Prapti"
    occupation="Software Developer"
    networth=1000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a= person()
a.name="Pranjal"
a.occupation="Footballer"
print(a.name,a.occupation)
a.info()
b= person()
b.name="Prakriti"
b.occupation="Actress"
print(b.name,b.occupation)
b.info()

# the self parameter is reference to current instance of thr class
