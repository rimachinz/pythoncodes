
import re
ch = input()
S = len(ch)
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(ch) == None):
    if 3 < S <= 10:


#row2
        for i in range(0, S, S):
            print(' '*(S+1), ch[i])
        print(' ' * (S), end='')

        for i in range(1, -1, -1):
            print(ch[i], end=' ')
        for i in range(1, 0, -1):
            print(ch[i])
            #row3
        print(' ' * (S - 2), end='')
        for i in range(2, -1, -1):
            print(ch[i], end=' ')
        for i in range(1, 3, 1):
            print(ch[i], end=' ')
        print()
            #row4
        print(' ' * (S - 8), end='')
        for i in range(3, -1, -1):
            print(ch[i], end=' ')
        for i in range(1, 4, 1):
            print(ch[i],end=' ')
        print()
            #row5
        print(' ' * (S - 2), end='')
        for i in range(0, S-1, 1):
            print(ch[i], end=' ')
        for i in range(1, -1, -1):
            print(ch[i], end=' ')
        print()
            #row6
        print(' ' * S , end='')
        for i in range(1, S-1, 1):
            print(ch[i], end=' ')
        for i in range(1, 0, -1):
            print(ch[i], end=' ')
        print()
            #row7
        for i in range(S-2, S, 2):
            print(' '*(S+1), ch[i])
    else:
        print("Wrong Constraints")

else:
    print("Wrong Constraints")








