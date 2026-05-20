f=open('myfile.txt','r') # r-------->reading, w-------->writing, a----------->append
print(f)
text=f.read()
print(text)
f.close()
# r is the default mode

f=open('myfile.txt','w') # r-------->reading, w-------->writing, a----------->append
print(f)
text=f.read()
print(text)
f.close()


# f=open('myfile.txt','a') # r-------->reading, w-------->writing, a----------->append
# print(f)
# text=f.append("You will ")
# print(text)
# f.close()

f=open('myfile.txt','a') # r-------->reading, w-------->writing, a----------->append
print(f)
text=f.write("You will")
print(text)
# f.close()

with open('myfile.txt','a'):
    f.write("You must")



