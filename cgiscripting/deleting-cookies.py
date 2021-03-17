#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
from http import cookies

c = cookies.SimpleCookie()
c['myCookie'] = ''
c['myCookie']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

# print the header, starting with the cookie
print(c)
print("Content-type: text/html\r\n\r\n")

# to verify cookie has been deleted run the retrieving_cookie.py again in the browser
print('''
<html>
<head>
    <title>Setting Cookies | Python CGI Programming</title>
</head>
<body>
<center>
    <h1>Cookie has been Set to Expire</h1>
</center>
</body>
</html>
''')