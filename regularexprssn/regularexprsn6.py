#match a  single chara
import re
string = '0123456789'
print('Matches =', re.findall('\d{2}',string))
print('Matches =', re.findall('\d{3}',string))
print('Matches =', len(re.findall('\d{5}',string)))
print('Matches =', re.findall('\d{5}',string))
