# #bubble sort
x = [x for x in input().split()]
l = len(x)

for i in range(l-1):
     for j in range(l-1-i):
         if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
print(x)
y =list(map(int,x))
print(y)
