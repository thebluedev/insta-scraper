import json
import re

# import os
with open("./plaintext/description.txt","r",encoding="utf-8") as descs:
    print("loaded script and ioFiles")
    data1 =descs.read()
    dataDict = json.loads(data1)
    # print(dict(data))
    # for i in dataDict
    print("loaded data")
    l=[]
    with open("./plaintext/hastags.txt","w+",encoding="utf-8") as hashfile:
        for data1 in dataDict:
            for innerData in data1.keys():
                splitted = data1[innerData].strip().split(" ")
                for i in splitted:
                    z = re.findall("^#\w+",i)
                    if z == []:
                        pass
                    else:
                        l+=z            
        print("iterated")
        hashfile.write(str(l))
    print("output to file.")
# print("shutting down")
# os.system('shutdown /p /f')