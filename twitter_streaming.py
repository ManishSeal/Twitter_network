#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import time

#Variables that contains the user credentials to access Twitter API
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

track_hashtags =['#fakenews']
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = track_hashtags[0]+timestr+".json"

# while mining the data (JSON) please add a [ in the beginning of the data and replace the , at the end of the JSON with a ] to make
# it a valid JSON file
class MyListener(StreamListener):
    def on_data(self, data):

        try:
            with open(file_name, 'a') as f:
                f.write(data+',')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=track_hashtags)
