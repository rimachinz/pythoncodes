#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>checkbox</title>")
print("</head>")
print("<body>")
print("<form action='6.cgi' method='post'>")
print("Subject")
print("<input type='checkbox' id='subject' name='maths'>Maths")
print("<input type='checkbox' id='subject' name='physics'>Physics<br>")
print("<input type='Submit' value='Submit'>")
print("</form>")
print("</body>")
print("</html>")



