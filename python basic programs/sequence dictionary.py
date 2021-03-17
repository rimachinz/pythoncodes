mydict = {}
print(mydict)

mydict[0] = 'ipsr'
mydict[1] = 'solutions'
mydict[2] = 'ltd'
print(mydict)

print(mydict.keys())#return key
print(mydict.values())#return all values

mydict.pop(0)#return value at index0
print(mydict)

mydict.popitem()#pop any key-value  pair
print(mydict)

mydict[0] = 'ipsr'
mydict[1] = 'solutions'
mydict[2] = 'ltd'
print(mydict)
print(str(mydict))
print(len(mydict))

newdict = mydict.copy()
print(newdict)
