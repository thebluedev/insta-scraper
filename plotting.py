import matplotlib.pyplot as plt
import json
plt.rcParams["figure.figsize"] = [50,50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
kr = {}
with open("./plaintext/finish.txt","r",encoding="utf-8") as f:
    fr = json.loads(f.read())
    
    for i in fr.keys():
        if fr[i]<11:
            continue
        else:
            kr[i] = fr[i]
    xpoints = sorted(kr.keys())
    ypoints = sorted(kr.values())
    plt.stem(xpoints, ypoints,)
    plt.show()