import urllib.request
import json
import urllib
from xml.etree import ElementTree as ET
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import clipboard

url = ""
keyword = ""
requestURL = ""
status = ""
message = ""
title = ""
short = ""


url = ""
while url == "":
    url = input("URL to shorten: ")
url = url.replace("&", "%26")

keyword = input("Enter a short link name: ")
if keyword == "":
    keyword = url.split("/")[-1]

requestURL = "https://shortener.tarundev.com/yourls-api.php" \
            + "?signature=92d16c5db3" \
            + "&action=shorturl" \
            + "&keyword=" + keyword \
            + "&format=json" \
            + "&url=" + url

root = urllib.request.urlopen(requestURL).read()
json = json.loads(root)
print('\n')

try:
    status = json['status']
    message = json['message']
    short = json['shorturl']
    title = json['title']
except:
    print(root)

out = "STATUS:\t\t" + status + "\n" \
    + "MESSAGE:\t" + message + "\n" \
    + "TITLE:\t\t" + title + "\n" \
    + "SHORTURL:\t" + short + "\n"
print(out)

clipboard.copy(short)