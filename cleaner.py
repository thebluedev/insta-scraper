"""NOT IN USE"""
import json
with open("./plaintext/finish.txt",'r',encoding='utf-8') as fin:
    finish = json.loads(fin.read())

    with open("./plaintext/finalISwear.txt",'r',encoding='utf-8') as fis:
        for i in finish.keys():
            if finish[i] < 11:
                pass
            else:
                