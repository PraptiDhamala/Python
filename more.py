f=open("myfile2.txt",'r')
while True:
    line = f.readline()
    # print(line)
    if not line:
        # print(line,type(line))
        break
    print(line)