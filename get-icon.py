
import json
import re
from urllib.parse import urlparse
import requests
import os.path
import os

HOST = "https://ted-developer.github.io/game-files"
LOCAL_WWW_ROOT = "/Users/yuanpeng01/Documents/code/game-cdn/cache"
LOCAL = os.path.dirname(__file__)

f = open("/Users/yuanpeng01/Downloads/download.json", "r")
list = json.loads(f.read())


for item in list:
    fileName = item['name']
    fileUrl = item['image_url']
    fielExt = re.search(".[^\.]+$", fileUrl).group(0)

    # save icon image
    strPath = "/images/icons/" + fileName + fielExt
    filePath = LOCAL + strPath
    if not os.path.exists(filePath):
        r = requests.get(fileUrl)
        img = open(filePath, 'wb')
        img.write(r.content)
        img.close()

    item['image_url'] = HOST + strPath

    # save game files
    urlPath = urlparse(item['url'])
    srcPath = os.path.dirname(LOCAL_WWW_ROOT + urlPath.path)
    strPath = "/pack/" + fileName + ".7z"
    filePath = LOCAL + strPath
    item['file'] = HOST + strPath

    print(srcPath)
    if not os.path.exists(filePath):
        # 压缩
        os.system("7z a "+filePath+" "+srcPath)

# save game list
gameList = open(LOCAL + "/game-list.json", 'w')
json.dump(list, gameList)