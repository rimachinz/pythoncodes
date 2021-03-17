#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

form=cgi.FieldStorage()
if form.getvalue('dropdown'):
    dropdown=form.getvalue('dropdown')
else:
    dropdown="not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>City</title>")
print("</head>")
print("<body>")
print("<h2>city is:%s</h2>"%dropdown)
print("</body>")
print("</html>")


