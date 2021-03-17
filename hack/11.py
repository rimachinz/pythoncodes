
T = int(input())
if - 1 <= T <= 100:

    count = 0
    start = int(input())
    end = int(input())

    for i in range(start, end+1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
            count += 1
        print(end='')
    print(count)
    for i in range(start, end+1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
            print(i,end=" ")
        print(end='')
else:
    print('Wrong Constraints')