#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
from http import cookies

# create a cookie and assign it a value
c = cookies.SimpleCookie()
c['myCookie'] = "it is my first cookie"

# cookie expiration time represented in milliseconds
c['myCookie']['expires'] = 1 * 1 * 3 * 60 * 60

# print the header, starting with the cookie
print(c)
print("Content-type: text/html\r\n\r\n")
print('''
<html>
<head>
    <title>Setting Cookies | Python CGI Programming</title>
</head>
<body>
<center>
    <h1>Cookie has been Set</h1>
</center>
</body>
</html>
''')