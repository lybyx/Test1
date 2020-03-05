import requests
import re
url="http://www.jd.com/"
data=requests.get(url).text
print(data)
pat='<title>.*?</title>'
datatitle=re.compile(pat,re.S).findall(data)
print('title:')
print(datatitle)