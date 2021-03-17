count=0
try:
    f=open('ipsr.txt')
    while True:
        c=f.read(1)
    if not c:
        print('end of file')
    break
    if c=='' or '\n':
        count+=1
except IOError as err:
    print('cant open file')
    print(err)
finally:
    print(count+1)
    f.close()
