# python3 ifelse.py
a=int(input("Enter you age : "))
print("Your age is ", a)
if(a>18):
    print("you can drive")
else:
    print("you cannot drive")
print(a>18)
print(a>=18)
print(a<18)
print(a<=18)
print(a==18)
print(a!=18)
# Indentation in python is equivalent to {} in c/c++
# if(a>18):
#     print("you can drive")
#     print("fah") in the if
# else:
#     print("you cannot drive")
#     print("hahah") in else
# # print("sakiyo") not in else 


# <---------- ELIF------------>
num=int(input("Enter any number: "))
if(num>0):
    print("Positive")
elif(num==0):
    print("Zero")
elif(num==-88):
    print("special")

# <------ Nested if-else ---------->
num1=10
if(num1<0):
    print("Number is negative")
elif(num1>0):
    if(num1<5):
        print("Number is lesser than 5")
    elif(num1>1 & num1<15):
        print("Number is between 1 and 15") 
    else:
        print("Number is greater than 5") 
else:
    print("zero")