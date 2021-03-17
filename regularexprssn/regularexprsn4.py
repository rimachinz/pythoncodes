# match series of ch range
import re
string = "Cat,Hat,Mat,Sat,Vat"
all_string = re.findall("[H-S]at", string)
for i in all_string:
    print(i)
