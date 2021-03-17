a=['i','p','s','r']
m=len(a)
for j in a:
    print(j, end=' ')
b = a[0:3]
b = b[::-1]
for j in b:
    print(j,end=' ')
print('\n')
k=2
for j in a[0:3]:
    print(j, end=' ')
print(end=k*' ')
k+=4

for j in b[0:3]:
    print(j,end=' ')
print('\n')
for j in a[0:2]:
    print(j,end=' ')
print(end=k*' ')
k+=4

for j in b[1:3]:
    print(j,end=' ')
print('\n')
for j in a[0:1]:
    print(j,end=' ')
print(end=k*" ")
k-=4

for j in a[0:1]:
    print(j,end=' ')
print('\n')
for j in a[0:2]:
    print(j,end=' ')
print(end=k*" ")
k-=4

for j in b[1:3]:
    print(j,end=' ')
print('\n')
for j in a[0:3]:
    print(j,end=' ')
print(end=k*' ')
for j in b[0:3]:
     print(j,end=' ')
print('\n')
for j in a[0:4]:
    print(j,end=' ')
for j in b[0:3]:
    print(j, end=' ')

