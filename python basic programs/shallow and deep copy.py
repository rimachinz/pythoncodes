a = [1, 2, 3, 4]
b = a
#print(b)

import copy
b = copy.copy(a)
#print(b)

b = copy.deepcopy(a)
#print(b)

from copy import copy
b = copy(a)
#print(b)

import copy
a=[[1,2,3] , [4,5,6]]
a.append([7,8,9])
#print(a)
b=copy.deepcopy(a)
#print(b)

import copy
b[1][1]='ipsr'#assignment operator (ref)



a=copy.deepcopy(b)#deep copy -ref not passed so no chnge in b affects a
print(b)
print(a)
b[0][1] = 44
print(b)
print(a)

a = copy.copy(b)# shallow copy
print(b)
print(a)
b[0][1] = 43
print(b)
print(a)
