import json
import os
import time
from subprocess import Popen

from dotenv import load_dotenv
from tweepy import StreamListener, Stream, OAuthHandler

from hdfs_sender import HDFSSender

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self, f, interval):
        self._f = f
        self._list_tweet = []
        self._list_thread = []
        self._interval = interval
        self._timestamp = 0

    def on_data(self, data):
        self._list_tweet.append(data)
        if time.clock() - self._timestamp > self._interval:
            self._timestamp += time.clock()
            HDFSSender(data, "hdfs:///user/hapoop/tweets").start()
        return True

    def on_error(self, status):
        print(status)


def auth(f, interval):
    l = StdOutListener(f, interval)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, l)
    return stream


f = open("tweet.json", "a")
stream = auth(f, 15)
stream.filter(track=['oui'])
print("daroit")
f.close()
