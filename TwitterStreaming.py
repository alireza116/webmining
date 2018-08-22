#install tweepy using: pip install tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# you need to create your api key from twitter developer portal
#consumer key, consumer secret, access token, access secret. UPDATE THESE TO THE ONES YOU OBTAIN.
ckey="fsdfasdfsafsffa"
csecret="asdfsadfsadfsadf"
atoken="asdf-aassdfs"
asecret="asdfsadfsdafsdafs"

#this class will be used to collect tweets
class listener(StreamListener):

    def on_data(self, data):
        # do stuff with the tweets. write to file, to db, etc
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

# authorize 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#start stream
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["charlotte"])