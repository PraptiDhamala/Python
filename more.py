# f=open("myfile2.txt",'r')
# while True:
#     line = f.readline()
#     # print(line)
#     if not line:
#         # print(line,type(line))
#         break
#     print(line)


# f=open("file3.txt",'r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     # print(line)
#     if not line:
#         # print(line,type(line))
#         break
#     m1=int(line.split(",")[0])
#     m2=int(line.split(",")[1])
#     m3=int(line.split(",")[2])
#     #m4=line.split(",")[3]

#     print(f"The Marks of student {i} in Maths is : {m1}  ")
#     print(f"The Marks of student {i} in MCSC is : {m2}  ")
#     print(f"The Marks of student {i} in DSA is : {m3} ")
#     # print(f"The Marks of student {i} in Network is{m4} : ")


# f=open("myfile3.tsx",'w')
# lines=['line 1\n' , 'line 2\n' , 'line 3\n']
# f.writelines(lines)
# f.close()

# #deals with positions seek and tell

# with open("myfile.txt",'r') as f:
#     f.seek(10)# moves to 10 bytes
#     data=f.read(6)
#     print(data)
#     current=f.tell()
#     print(current)

with open("samp.txt",'w') as f:
    f.write("Hello Papu Don !!")# moves to 10 bytes
    f.truncate(6)

with open("samp.txt",'r') as f:
    print(f.read())