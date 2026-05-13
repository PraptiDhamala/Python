for i in range(9):
    print(i)
else:
    print("Cannot find i")


for i in range(9):
    print(i)
    if i == 4:
        break
else:
    print("Cannot find i")

i=0
while i<9:
    i=i+1
    print(i)
    if i == 4:
        break
else:
    print("Cannot find i")