#program to find the count of nos in a digit
digit = int(input())
count = 0
while digit != 0:
    digit = digit //10
    count+=1
print(count)