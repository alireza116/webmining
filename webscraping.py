from bs4 import BeautifulSoup
import json
import requests
import time
import random

r = requests.get("http://tsear.ch/list/fa/100")

soup = BeautifulSoup(r.text, "lxml")
dataset = []
channels = soup.find_all("div",{"class":"media heading-divided"})
for channel in channels[1:]:
    title = channel.find("div",{"class":"media-heading"}).find("a",href=True)
    link = title["href"]
    cTitle = title.text
    desc = channel.find("div",{"class":"overflow-hidden"}).text
    channelAddress = channel.find("div",{"class":"media-annotation"}).text

    channelAddress = [i.strip() for i in channelAddress.split(" ")]
    cAddress = channelAddress[0]
    numFollowers = channelAddress[1]
    data = {
        "title":cTitle,
        "tsearchLink":"http://tsear.ch"+link,
        "description":desc,
        "handle":cAddress,
        "numFollowers":numFollowers
    }
    dataset.append(data)

with open("telegramChannels.json","w") as datasetFile:
    datasetFile.write(json.dumps(dataset))