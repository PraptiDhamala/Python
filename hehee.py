# Basic Python example: greeting and simple math

def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

# Main program
if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum:", add_numbers(x, y))