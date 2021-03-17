#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

form=cgi.FieldStorage()
if form.getvalue('Sex'):
    Sex=form.getvalue('Sex')
else:
    Sex="not set"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>mycgi</title>")
print("</head>")
print("<body>")
print("<h2>Sex is:%s</h2>"%Sex)
print("</body>")
print("</html>")


