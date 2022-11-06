import json

l = []
with open("./saved/saved_posts.json","r") as collections:
    data = json.load(collections)
    linksFile = open("Links.txt","w+")
    for post in data["saved_saved_media"]:
        linksFile.write(post["string_map_data"]["Shared By"]["href"]+"\n")
    linksFile.close()

    for post in data["saved_saved_media"]:
        if post["string_map_data"]["Shared By"]["value"] not in l:
            l.append(post["string_map_data"]["Shared By"]["value"])
    posterFile = open("Poster.txt","w+")
    for i in l:
        posterFile.write(i+"\n")
    posterFile.close()