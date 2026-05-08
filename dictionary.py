dic={'name':"Prapti", 'age':19, 'address':'Suncity' }
# print(dic)
# print(dic.keys())
# print(dic.values())

# for key in dic.keys():
#     print(dic[key])

# dic={'name':"Prapti", 'age':19, 'address':'Suncity' }
# dic2={'surname':"Dhamala"}
# dic.update(dic2)
# print(dic,dic2)
# dic.clear()
dic.popitem()
print(dic)
dic.pop('age')
print(dic)
del dic['name']
print(dic)
