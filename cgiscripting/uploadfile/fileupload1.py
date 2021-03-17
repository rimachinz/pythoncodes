#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"
import cgi
print("Content-type:text/html\r\n\r\n")
print('''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File Upload | Python CGI Programming</title>
</head>
<body>
    <center>
        <form action="fileupload.cgi" enctype="multipart/form-data" method="post">
            <br><br><br><br><br><br><br><br><br><br><br>
            File : <input type="file" name="myfile" id="myfile"><br><br>
            <input type="submit" value="Upload">
        </form>
    </center>
</body>
</html>
      ''')