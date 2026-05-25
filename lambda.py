def appl(fx, value):
    return 6+fx(value)

# print(double(5))


triple = lambda y: y*3
cube = lambda y : y*y*y
avg = lambda x,y : (x+y)/2
avgi = lambda x,y,n : (x+y)/n

print(triple(5))
print(cube(5))
print(avg(10,5))
print(avgi(10,5,5))
print(appl(cube,2))
#  python3 lambda.py