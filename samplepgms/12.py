#print smallest divisor of an integer
n=int(input())
for i in range(2,n,1):
    if n % i == 0:
        print(i)
        break
#print largest divisor of an integer
for i in range(n-1,2,-1):
    if n % i == 0:
        print(i)
        break
