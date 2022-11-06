""" TODO implement counter, import hashtags.txt and convert to text, 
then loop over it and hashtags.txt and use count() to determine frequence"""

strn = ""
print("starting...")
with open("./plaintext/hastags.txt","r",encoding="utf-8") as hastagsFile:
    print("file opened")
    hashtags = hastagsFile.read().split(",")
    print("file read")
    print("number of hashtags")
    print(len(hashtags))
    noDupes = set(hashtags)
    print("number of unique hashtags")
    print(len(noDupes))
    for hashtag in noDupes:
        num = hashtags.count(hashtag)
        strn += hashtag+","+str(num) + "\n"
    with open("./plaintext/finish2.txt","w+",encoding="utf-8") as finish:
        finish.write(strn)



