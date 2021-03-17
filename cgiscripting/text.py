#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>My first CGI program</title>")
print("</head>")
print("<body>")
print("<form action='5.cgi' method='post'>")
print("FirstName:<input type='text' id='first_name' name='first_name'></br>")
print("LastName:<input type='text' id='last_name' name='last_name'></br>")
print("<input type='Submit' value='submit'>")
print("</form>")
print("</body>")
print("</html>")