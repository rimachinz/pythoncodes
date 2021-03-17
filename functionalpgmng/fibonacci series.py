
n = int(input("enter number of digits you want in series (minimum 2): "))
first = 0
second = 1
for i in range(1, n):
    next = first + second
    print(next, end=" ")
    first = second
    second = next