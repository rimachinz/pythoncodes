import re
File='test.txt'
Fileobj=open(File,'r')
#input string
# Fileobj.write(input('string=',))
s = Fileobj.read()
#string display
print(s)
#count of words
print(len(s.split()))
##count of vowels
allstring=re.findall('[aeiouAEIOU]',s)
count=0
for i in allstring:
    count+=1
print(count)
Fileobj.close()
