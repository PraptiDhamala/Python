def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return(num * factorial(num-1))

num=int(input("Enter any number:")) #int halnu parcha hai agadi
print("The number is: ",num)
print("The factorial of the number is: ",factorial(num))