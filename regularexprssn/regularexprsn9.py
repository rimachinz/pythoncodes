#check phonenumber
import re
if re.match(r'\+91-[0-9]{4}-[0-9]{3}-[0-9]{3}', '+91-8592-080-967'):
    print('its a valid number')
if re.search(r'\d{4}-\d{3}-\d{3}', '8592-080-967'):
    print('its a valid number')