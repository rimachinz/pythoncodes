#prime no
N = int(input())
if N >= 5:
    l = list(map(int, input().split(' ')))[:N]
    x = len(l)
    list1= []
    # count = 0
    for i in range(0,x):
        count = 0
        for j in range(2, l[i]):
            if l[i] % j == 0:
                count += 1
        if count == 0:
            list1.append(l[i])
    if count == 0:
        p = 1
        for i in range(len(list1)):
            p*=list1[i]
        print(p)
    elif count != 0:
        print("No Prime numbers")
    else:
        print()
# print(list1)




