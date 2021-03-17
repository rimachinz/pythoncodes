#print prime factors of an integer
x = int(input())
k, e =[], []
for i in range(1,x+1):
    if x % i == 0:#finding factors of x
        k.append(i)
    print(end='')
print(k)
for i in k:
    count = 0
    if k % i == 0:
        count +=1
    if count <= 2:
        print(k)