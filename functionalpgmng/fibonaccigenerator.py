
def fibonacci(n):
    a, b, counter = 0, 1, 0
    # print('hi')
    while True:
        # print('he')
        if counter == n:
            return
        else:
            yield a
            a, b = b, a + b
            counter += 1
f = fibonacci(4)
# print(f)#returns location of generator object
for x in f:
    print(x, " ", end="")

