#web scraping
import re
import urllib as u
import urllib.request
import webbrowser

url = "http://www.corporationoftrivandrum.in/phone-numbers"

response = u.request.urlopen(url)# request to open the file
#print(response)
html = response.read() # read the file
#print(html)
htmlstr = html.decode()
#print(htmlstr)
#htmlstr = u.request.read().decode() # request,read and decode in a single line
pdata = re.findall('0471-\d{7}|0471\d{7}|2\d{6}', htmlstr)#scraping numbers in required format
for i in pdata:
    print(i)

