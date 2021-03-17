a=[1,2,3,4,5]
i=0
while True:
    try:
        print(a[i])

    except IndexError as err:
        print(err)
        break
    else:
        i+=1
        print(i)
