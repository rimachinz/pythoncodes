#read a number and print the sum of IST n numbers
n = int(input())
sum=0
for i in range(n+1):
    sum+=i
print("1+2+3+...",n,"=",sum)
#using formulae
sum1=(n*(n+1))//2
print(sum1)