#/usr/bin/env python3
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'FfJKXQTM0qnyhZn2KeWiyCP3t'
consumer_secret = '9i9syT4UfZ2xM6AXBOV2gqC2VP3hkMS3NmjYnRsVe23Mey63BK'
access_token = '121657099-zKlOiAsPXoMqrKyLV1amjYYZskfWzWSVRjEkD5Bv'
access_secret = 'rI5wSDho5APyPfznKwwbJ4rem2SnVgO0QezAxg6k3fbF3'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

"""
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
"""
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f: # Submit to google form to generate email notifications
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#malware'])