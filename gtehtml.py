import requests
import re
url="http://www.baidu.com/"
data=requests.get(url).text
print(data)
pat='<title>.*?</title>'
datatitle=re.compile(pat,re.S).findall(data)
print('title:')
print(datatitle)