try:
    f=open('ipsr.txt')
    for line in f:
        print(line,end='')
except IOError:
    print('cant find file')
finally:
    f.close()
