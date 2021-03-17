# read the no and print the natural nos summation pattern
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
    print("1+2+3+...",i,"=",sum)