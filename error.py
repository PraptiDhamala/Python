a=input("Enter any number: ")
print(f"Multiplication table of {a} is :")
try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
print("Some imp lines of codes")
print("End of program ")

a=input("Enter any number: ")
print(f"Multiplication table of {a} is :")
try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!!!")
print("Some imp lines of codes")
print("End of program ")