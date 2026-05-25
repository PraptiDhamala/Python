# def cube(x):
#     return x*x*x

# print((cube(2)))

# # python3 filter.py
# l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))
# # newl= list(map(cube,l))
# print (newl)    


# p=[1,9,4,8,4,3,7]
# newl= list(map(cube,p))
# print (newl)    

# def filter_function(a):
#     return a>2

# newnewl= list(filter(filter_function,l))
# print(newnewl)

# REDUCE

from functools import reduce
numbers=[1,2,3,4,5]

sum=reduce(lambda x,y: x+y, numbers)
print(sum)