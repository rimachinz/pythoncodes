a, b = 0, 1
for i in range(int(input('enter limit : '))):
    print(a, end=" ")
    a, b = b,a+b
