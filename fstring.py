letter="Hey my name is {} and I am from {}"
country="Nepal"
name="Prapti"
print(letter.format(name,country))
# python3 fstring.py
letter="Hey my name is {1} and I am from {0}"
country="Nepal"
name="Prapti"
print(letter.format(name,country))
# fstring
print(f"Hey my name is {name} and I am from {country}")

price=99.00011111
txt=f"The price of the product is {price: .2f}"
print(txt)
