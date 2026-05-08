def fibonacci(num):
    if(num<=0):
        return 0;
    elif (num==1):
        return 1;
    else:
        return(fibonacci(num-2)+fibonacci(num-1));


num=int(input("Enter any number: "))
print("The fibonacci series is: \n")
for i in range(num):
    print(fibonacci(i), end=" ")