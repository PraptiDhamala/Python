marks=[12,2,3,44,89,98]
index=0
for mark in marks:
    print (mark)
    if(index==3):
        print("I am the donnn")
    index +=1

for index, mark in enumerate(marks):
    print (mark)
    if(index==3):
        print("I am the donnn")
    # index +=1
for index, mark in enumerate(marks,start=1):
    print (mark)
    if(index==3):
        print("I am the donnn")
    # index +=1


