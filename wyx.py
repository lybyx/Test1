#test
import requests
import re

url="http://www.jd.com/"
data=requests.get(url)

pat="<title>.*?</title>"

gettitle=re.compile(pat,re.S).findall(data.text)


if __name__=="__main__"
data.text
gettitle
