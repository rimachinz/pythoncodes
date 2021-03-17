#Check if a Date is Valid and Print the Incremented Date if it is
date=input()
dd,mm,yy = date.split('/')
print(dd,mm,yy)
dd = int(dd)
mm = int(mm)
yy = int(yy)

if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm ==12):
    max1 =31
elif (mm == 4 or mm ==6 or mm == 9 or mm == 11):
    max1 = 30
elif(yy % 4 ==0):
    max1 =29
else:
    max1 =28
if mm < 1 or mm > 12:
    print('invalid date')
elif dd < 1 or dd > max1:
    print('invalid date')
elif dd == max1 and mm != 12:
    dd =1
    mm += 1
    print('incremented date is',dd,mm,yy)
elif dd == max1 and mm ==12:
    dd = 1
    mm = 1
    yy += 1
    print('incremented date is',dd,mm,yy)
else:
    dd += 1
    print('incremented date is',dd,mm,yy)

