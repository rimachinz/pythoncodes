# star pattern
n = int(input())
# right aligned increasing star pattern
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     print('\n')
#left aligned increasing star pattern
# for i in range(0, n+1, 1):
#     for j in range(i, 0, -1):
#         print("*", end=" ")
#     print('\n')

#increasing star pattern
# for i in range(1, n+1, 1):
#     print((n-i)*" "+i*"*")
# inverted triangle
# for i in range(n, 0, -2):
#     j=i//2
#     print((n-j)*" "+i*"*"+(n-j)*" ")
def triangle(n):
    k = 2 * n-2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
triangle(n)