#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi,cgitb
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Textbox</title>")
print("</head>")
print("<body>")
print("<form action='textbox8.cgi' method='post' target = '_blank'>")
print("Address")
print("<textarea name = 'Address' cols = '40' rows = '4'></textarea>")
print("<input type='Submit' value='Submit'>")
print("</form>")
print("</body>")
print("</html>")
