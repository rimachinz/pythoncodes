#!"C:\Users\RIMA RAFEEK\AppData\Local\Programs\Python\Python37-32\python.exe"

import cgi
import os
print('content-type:text/html\r\n\r\n')
print('<font size=+1>Environmentvariables</font></br>')
for i in os.environ.keys():
    print('<b>%20s</b>: %s<br>'%(i,os.environ[i]))