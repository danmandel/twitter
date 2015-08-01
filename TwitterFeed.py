from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'oIkifLfqNy9ubpr3gJPCpEMAM'
csecret = 'IqAyLmnmw5TXsBtCBM1G8UTUsPsngqX8vJL8WmYhdyZ3VhnS8L'
atoken = '2471933238-MyaUvm4O6ikqwsvytkqgnvFSYXdPFSebHIll88n'
asecret = 'bnDehlfEE1W3ZXhJb0wckakrSC6yYHYE67TW4sH7VbYSr'

class listener(StreamListener):

    def on_data(self, data):
        try:
            print (data)
            saveFile = open('twitdb.csv','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()  
            return True
        except BaseException, e:
            print 'failed ondata, ', str(e)
            time.sleep(5)
    
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["gilinsky"])
