#print odd nos in a given range
start_range = int(input())
end_range = int(input())
for i in range(start_range,end_range,1):
    if i%2 != 0:
        print(i,end=" ")
    print(end="")