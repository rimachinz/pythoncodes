t = int(input())
if 1 <= t <= 100:
    for i in range(t):
        a, b, c = [], [], []
        x=0
        for i in input():
            a.append(i)
        for i in input():
            b.append(i)
        if 0 < len(a) <= 10 and 0 < len(b) <= 10:
            for i in a:
                for j in b:
                    if i == j:
                        c.append(j)
                        b.remove(j)
                        x += 1
            if x == 0:
                print(x)
                print('()')
            else:
                print(x)
                print('(', end='')
                for i in range(len(c)-1):
                    print(c[i], end=',')
                print(c[len(c)-1], end=')')
                # print(c)
        else:
            print("String Length Exceeded")
else:
    print("Limit Exceeded")
