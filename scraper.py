import json
import os
import time
import urllib.request as requests

from bs4 import BeautifulSoup

descriptions = {}
with open("./plaintext/Links.txt","r") as linksFile:
    links = linksFile.readlines()
    cter =0
    descs =open("./plaintext/Description.txt","w+")
    for link in links:
        time.sleep(0.1)
        link=link.replace("\n", "")
        # Requseting url
        req =requests.Request(link)
        # opening requested url
        f =requests.urlopen(req)
        # reading and decoding url data
        page = f.read().decode('utf-8')
        # parse data with bs
        soup = BeautifulSoup(page, "html.parser")
        # selecting description from data
        try:
            text = soup.find('meta',property="og:description").get("content",None)
            # creating dict to store url:description pairs
            descriptions[link]=text
        except AttributeError:
            print("ERROR OCCURED",cter)
            pass
        cter+=1
    descs.writelines(json.dumps(descriptions))
    descs.close()
os.system("shutdown /f /q")