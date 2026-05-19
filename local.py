x=9
print(x)
print(f"The global x is {x}")


def hello():
    x=5
    print(f"The local value is {x}")
    print("Hi papu")
print(f"The global x is {x}")
hello()
x=5
print(f"The global x is {x}")
def hello():
    global x
    x=5
    print(f"The local value is {x}")
    print("Hi papu")
hello()
print(f"The global x is {x}")

x=4
print(f"The global x is {x}")
