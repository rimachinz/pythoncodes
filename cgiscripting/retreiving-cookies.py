#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import os
from http import cookies

print("Content-type: text/html\r\n\r\n")
print('''
<html>
<head>
    <title>Retrieving Cookies | Python CGI Programming</title>
</head>
<body>
<center>
    <h1>Check the cookie</h1>
''')
if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = cookies.SimpleCookie()
    c.load(cookie_string)

    try:
        data = c['myCookie'].value
        print("Cookie data : ", data)
    except KeyError:
        print("The cookie was Not Set or has Expired")
print('''
</center>
</body>
</html>
''')