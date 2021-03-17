#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi
form=cgi.FieldStorage()
first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>mycgi</title>")
print("</head>")

print("<body>")
print("<h2>First Name is:%s</h2>"%first_name)
print("<h2>Last Name is:%s</h2>"%last_name)

print("</body>")
print("</html>")

