#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

form=cgi.FieldStorage()
if form.getvalue('maths'):
    math_flag="ON"
else:
    math_flag="OFF"
if form.getvalue('physics'):
    physics_flag="ON"
else:
    physics_flag="OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>mycgi</title>")
print("</head>")
print("<body>")
print("<h2>Checkbox Maths is:%s</h2>"%math_flag)
print("<h2>Checkbox Physics is:%s</h2>"%physics_flag)
print("</body>")
print("</html>")

