
import json
import re
import requests

f = open("/Users/yuanpeng01/Downloads/download.json", "r")
list = json.loads(f.read())

for item in list:
    fileName = item['name']
    fileUrl = item['image_url']
    fielExt = re.search(".[^\.]+$", fileUrl).group(0)

    r = requests.get(fileUrl)

    img = open("images/icons/" + fileName + fielExt, 'wb')
    img.write(r.content)
    img.close()