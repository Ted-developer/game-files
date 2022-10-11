
import json
import re
import time
from urllib.parse import urlparse
import requests
import os.path
import os
from webpc import convert
from itertools import cycle

HOST = "https://ted-developer.github.io/game-files"
LOCAL_WWW_ROOT = "/Users/xiaodugame/Documents/work/code/get-game/cache"
LOCAL = os.path.dirname(__file__)
key = [9]

f = open("/Users/xiaodugame/Downloads/download.json", "r")
list = json.loads(f.read())


def encryteFile(name):
    file = open(name, "r")

    # 加密
    byte = bytes(file.read(), 'utf-8')
    encrypted = [a ^ b for (a, b) in zip(byte, cycle(key))]

    fw = open(name, "wb")
    fw.write(bytes(encrypted))


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
    #if os.path.exists(filePath):
        os.system("rm -rf /tmp/*")
        os.system("cp -r " + srcPath + " /tmp/" + fileName)
        # image to webp
        convert("/tmp/" + fileName)

        # 加密js、json文件
        for subdir, dirs, files in os.walk("/tmp/" + fileName):
            for file_name in files:
                if file_name.endswith('.js') or file_name.endswith('.json'):
                    #print(os.path.join(subdir, file_name))
                    encryteFile(os.path.join(subdir, file_name))

        # 压缩
        #os.system("7z a "+filePath+" "+srcPath)
        os.system("7z a "+filePath+" /tmp/"+fileName)

# save game list
gameList = open(LOCAL + "/game-list.json", 'w')
jsonData = {'game_list': list, 'update_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
json.dump(jsonData, gameList)