#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

form=cgi.FieldStorage()
if form.getvalue('Address'):
    Address=form.getvalue('Address')
else:
    Address="not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>mycgi</title>")
print("</head>")
print("<body>")
print("<h2>Address is:%s</h2>"%Address)
print("</body>")
print("</html>")


