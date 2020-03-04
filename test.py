#testfile

import requests
url='http://www.jd.com'
data=requests.get(url).text
print(data)