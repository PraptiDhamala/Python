# decorator is a function that takes another function as an argument and return new func that modifies the behaviour of original one
def greet(fx):
    def mfx(*args, **kwargs):
        print("Goodmorning")
        fx(*args, **kwargs)
        print("Thanks for using the function")
    return mfx

@greet
def hello():
    print("Hiiii WOrldiessss")
@greet
def add(a,b):
    print(a+b)

hello()
add(3,5)