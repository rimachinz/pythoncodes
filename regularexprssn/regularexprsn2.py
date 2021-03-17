import re
NameAge ='''
Bismi is 10 and Remya is 20
Nisha is 24 and Ansu is 25
'''
ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1
print(ageDict)
