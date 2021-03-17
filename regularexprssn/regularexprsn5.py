# replace a string
import re
string = "Cat,Hat,Mat,Rat,Sat,Vat"
regex = re.compile("[R]at") # finding rat nd replacing it with dog
substring = regex.sub('Dog', string) # substituting using sub()
print(substring)
