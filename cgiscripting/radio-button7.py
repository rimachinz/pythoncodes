#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi,cgitb
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>radio</title>")
print("</head>")
print("<body>")
print("<form action='radio-button7.cgi' method='post' target = '_blank'>")
print("Sex")
print("<input type='radio' name='Sex' value='male'>Male")
print("<input type='radio' name='Sex' value='female'>Female<br>")
print("<input type='Submit' value='Submit'>")
print("</form>")
print("</body>")
print("</html>")
