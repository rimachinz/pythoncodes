x = [x**2 for x in range(20)]
# print(x)

not_prime = [j for i in range(2, 8) for j in range(i*2, 100, i)]
# print(not_prime)

prime = [x for x in range(2, 100) if x not in not_prime]

# print(prime)
x = [1, 2, 3]
y = [4, 5, 6]
z = [(i, j) for i in x for j in y]
print(z)

mysum = lambda x, y: x+y
print(mysum(2, 3))
