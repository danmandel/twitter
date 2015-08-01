from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'oIkifLfqNy9ubpr3gJPCpEMAM'
csecret = 'IqAyLmnmw5TXsBtCBM1G8UTUsPsngqX8vJL8WmYhdyZ3VhnS8L'
atoken = '2471933238-MyaUvm4O6ikqwsvytkqgnvFSYXdPFSebHIll88n'
asecret = 'bnDehlfEE1W3ZXhJb0wckakrSC6yYHYE67TW4sH7VbYSr'

class listener(StreamListener):

    def on_data(self, data):
        print (data)
        return True
    
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
