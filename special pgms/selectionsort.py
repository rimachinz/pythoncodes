# #selection sort

a = [16, 19, 11, 15, 10, 12, 14]
i = 0
while i < len(a):
    #smallest element in the sublist
    small = min(a[i:])

    #index of smallest element
    pos = a.index(small)
    print(pos)
    #swapping
    a[i],a[pos] = a[pos],a[i]
    i=i+1
print (a)