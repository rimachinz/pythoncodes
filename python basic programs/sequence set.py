a={1,2,3,4,}
b={3,4,5,6}
print(a)

print(a.union(b))

print(a|b)

print(a.intersection(b))
print(a&b)

print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)


print(a.symmetric_difference(b))
print(a^b)

a.add(7)
print(a)

a.clear()
print(a)
