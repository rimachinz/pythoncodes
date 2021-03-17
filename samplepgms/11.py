#find sum of digits in a number
x=int(input())
sum = 0
while x!=0:
    rem = x%10
    sum += rem
    x = x//10
print(sum)
