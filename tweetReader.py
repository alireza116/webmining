import json
from pprint import pprint

data = []
with open("kanyeWest.txt","r",encoding="UTF-8") as jsonFile:
    for line in jsonFile:
        try:
            data.append(json.loads(line))
        except:
            pass

for i, tweet in enumerate(data):
    print(tweet["text"])
    print(tweet["user"]["id_str"])
    print("-----")
    if i == 100:
        break