import re
N = int(input())

l = input()
j =input() in ('+','-','/')
if j == '+':
    print()
elif j == '-':
    print()
elif j == '/':
    print()
else:
    print('wrong operator: only arithmetic operators are allowed')
matches= re.findall(r'\d{2}', l)

print('matches:', re.findall(r'\d{2}', l))
# print(type(l))
# for i in range(matches):
    # if matches[i] and matches[i+1] in l
matches=list(map(int,matches))
print(sum(matches))