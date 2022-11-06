import matplotlib.pyplot as plt
import json
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
    plt.plot(xpoints, ypoints)
    plt.show()