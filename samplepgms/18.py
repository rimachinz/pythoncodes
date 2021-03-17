#identity matrix
rows = int(input())
for i in range(rows):
    for j in range(rows):
        if i == j:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print('\n')
