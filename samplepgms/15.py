#print integers in a range not divisible by 2 or 3
start_range = int(input())
end_range = int(input())
for i in range(start_range,end_range+1,1):
    if i % 2 == 0:
        print(end="")
    elif i % 3 == 0:
        print(end="")
    else:
        print(i, end=" ")
    print(end="")
