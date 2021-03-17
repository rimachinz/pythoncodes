import math
#binary search
x =[int(x) for x in input().split()]
print(x)
n = int(input())
l = len(x)
start = 0
end = l-1
mid = math.floor((l-1) // 2)
# print(mid)
x = sorted(x, reverse=False)
if n == x[mid]:
    print('element found at mid position',(mid+1))
elif n > x[mid]:
    for i in range(mid+1,end+1):
        if n == x[i]:
            print('element at',(i+1))
        print(end='')
    print()
elif n < x[mid]:
    for j in range(0, mid):
        if n == x[j]:
            print('element at', (j+1))
        print(end='')
    print()
else:
    print()


