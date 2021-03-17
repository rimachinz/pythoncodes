#palindrome or not
a = ['m', 'a', 'l', 'a', 'y', 'a', 'l', 'a', 'm']
# a=['i','p','s','r']

b = len(a)//2

c = len(a)
e = a[0:b]
d = a[b+1:c]
d = d[::-1]
if e == d:
    print('yes')
else:
    print('no')

