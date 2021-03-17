#linear search
z = int(input())
y =[int(x) for x in input().split()]
n = len(y)
print(y)
for i in range(n):
    if y[i] == z:
        print('element found at:',i+1)