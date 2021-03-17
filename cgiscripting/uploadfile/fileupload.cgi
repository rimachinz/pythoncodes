#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['myfile']

# Test if the file was uploaded
if fileitem.file:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('uploadfile/' + fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print('''Content-type: text/html\r\n\r\n
<html>

<body>
   <p>%s</p>
</body>
</html>
''' % (message,))
