# to print element in string of length 5 to 7
import re
string = '12 123 1234 12345 123456 1234567 '
print('matches:', re.findall("\d{5,7}", string))