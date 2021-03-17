def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    # print('hi')
    while True:
        # print('he')
        yield a
        a, b = b, a + b


f = fibonacci()

counter = 0
for x in f:
    if counter >= 5:
        break
    print(x, " ", end="")
    counter += 1

