# Without walrus
line = input("Enter text (or 'quit'): ")
while line != "quit":
    print(f"You said: {line}")
    line = input("Enter text (or 'quit'): ")

# With walrus
while (line := input("Enter text (or 'quit'): ")) != "quit":
    print(f"You said: {line}")