import urllib.request as ET
import json

url='http://py4e-data.dr-chuck.net/comments_2224738.json'
data=ET.urlopen(url).read()
info=json.loads(data)

count=0
total=0

for iten in info["comments"]:
    count+=1
    total+=int(iten["count"])
print(count)
print(total)