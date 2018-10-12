#install tweepy using: pip install tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# you need to create your api key from twitter developer portal
#consumer key, consumer secret, access token, access secret. UPDATE THESE TO THE ONES YOU OBTAIN.
ckey="7o9au5o3jE8G57iMSd4zjnEin"
csecret="D4EkOCWRDlXQDlF8WnQnbvMgWoTGxIhitU9iBNZKAu7M70jKHg"
atoken="2327831132-spuOdDrzUuoaYXFt59iDjQUx00YdV6kmhemK4SR"
asecret="QmT2Na3naObKA9TZLJcj9kbdL2beVavi3ae8bCwmW0eFw"

# consumer_key="7o9au5o3jE8G57iMSd4zjnEin"
# consumer_secret="D4EkOCWRDlXQDlF8WnQnbvMgWoTGxIhitU9iBNZKAu7M70jKHg"
# access_token="2327831132-spuOdDrzUuoaYXFt59iDjQUx00YdV6kmhemK4SR"
# access_token_secret="QmT2Na3naObKA9TZLJcj9kbdL2beVavi3ae8bCwmW0eFw"

#this class will be used to collect tweets
class listener(StreamListener):

    def on_data(self, data):
        # do stuff with the tweets. write to file, to db, etc
        tweet = json.loads(data)
        print(tweet["text"])
        with open("kanyeWest.txt","a") as outFile:
            outFile.write(data + "\n")
        # print(data)
        return(True)

    def on_error(self, status):
        print(status)

# authorize 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#start stream
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["kanye west"])