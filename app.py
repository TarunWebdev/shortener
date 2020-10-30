from flask import Flask , render_template , redirect , url_for , request
import urllib.request
import json
import urllib
from xml.etree import ElementTree as ET
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/shortener',methods=['GET','POST'])
def short():
    if request.method=='POST':
        longurl = request.form['longurl']
        custom = request.form['custom']
        if not longurl and custom:
            return 'Error <script>alert("Invalid Credentials");</script>'
        if longurl.startswith("http://" or "https://"):
            pass
        else:
            longurl = str("http://"+str(longurl))

        url = ""
        keyword = ""
        requestURL = ""
        status = ""
        message = ""
        title = ""
        short = ""


        url = longurl
        
        url = url.replace("&", "%26")

        keyword = custom
        if keyword == "":
            keyword = url.split("/")[-1]

        requestURL = "http://shortener.tarundev.com/yourls-api.php" \
                    + "?signature=92d16c5db3" \
                    + "&action=shorturl" \
                    + "&keyword=" + keyword \
                    + "&format=json" \
                    + "&url=" + url

        root = urllib.request.urlopen(requestURL).read()
        jsonn = json.loads(root)

        try:
            status = jsonn['status']
            message = jsonn['message']
            short = jsonn['shorturl']
            title = jsonn['title']
        except:
            print(root)

        out = "STATUS:\t\t" + status + "\n" \
            + "MESSAGE:\t" + message + "\n" \
            + "TITLE:\t\t" + title + "\n" \
            + "SHORTURL:\t" + short + "\n"

        url = "https://shortener.tarundev.com/"+custom

        return 'Live at <a target="_blank" href="'+url+'">'+url+'</a><p>'+out+'</p>'
    return ""

if __name__ == "__main__":
    app.run()