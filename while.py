# i=int(input("Enter number: "))
# # i=0
# while(i<=15):
#     print(i)
#     i=i+1
#     print("Done with loop ",i)
# print("Done with loop it ")

# count=90
# while(count>=80):
#     print(count)
#     count=count-1
# else:
#     print("I am not in loop")


# # <----------- Break and Continue Statement------------------>

# for i in range(12):
#     if(i==5):
#         break
#     print("5 X ",i+1," = ", 5*(i+1) )
# #Breaking out of loop, loop bata nai bahira auacha if mailee i=5 liye vane aba i=5 ra tesko tala ko execute hunna 


# for i in range(12):
#     if(i==5):
#         continue
#     print("5 X ",i+1," = ", 5*(i+1) )
# #skips the iteration


# Emulate do while loop 

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
