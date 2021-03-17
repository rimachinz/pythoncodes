#mail
import re
mail1 = 'rimarafeek@gmail.com'
mail2 = 'noufila.l@gmail.co.uk'
mail3 = 'qqqqqqqqqqwwwwwwwwwweeeeeeeeeerrrrrrr@gmail.com'
mail4 = 'nisha.susan21@gmail.com'
mail5 = 'nishasm%athew@gmail.com'
if re.search(r'^[a-z0-9_.]{1,20}@[a-z]{1,20}(\.[a-z]{2,3}){1,2}$', mail2):
    print('validmail')

if re.search(r'^[a-z0-9_.]{1,20}@[a-z]{1,20}(\.[a-z]{2,3}){1,2}$', mail4):
   print("its a valid email")

