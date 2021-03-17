# match word
import re
string = "Cat,Hat,Mat,Sat,Vat"
all_string = re.findall('[HSVMC]at', string)
for i in all_string:
    print(i)


