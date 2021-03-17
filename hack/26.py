#paṭṭērn printing
for i in range(5):
    for j in range(i):
        print(i, end='')
    print()
for i in range(6):
    for j in range(1,i):
        print(j, end='')
    print()
s = 1
for i in range(5):
    for j in range(1,i+1):
        print(s, end=' ')
        s += 1
    print()