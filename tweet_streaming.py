import json
import os
import time

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
        self._filepath = f
        self._list_tweet = []
        self._list_thread = []
        self._string_tweet=""
        self._interval = interval
        self._timestamp = time.time()


    def on_data(self, data):
        self._string_tweet+=data+'\n'
        if time.time() - self._timestamp > self._interval:
            print("SENDING "+str(len(self._list_tweet)) +" tweets TO HDFS...")
            self._timestamp = time.time()
            HDFSSender(self._string_tweet, "hdfs://master.sagean.fr:8020/user/hapoop/tweets_dir/time="+str(int(time.time()))).start()
        return True

    def on_error(self, status):
        print(status)

    def save(self):
        with open(self._filepath, "w") as f:
            f.write(self._list_tweet)
            print("Saving "+str(len(self._list_tweet)) + " tweets")

    def load_json(self):
        print("Load json")
        with open(self._filepath) as file:
            self._list_tweet = json.load(file)
            print("there are : "+str(len(self._list_tweet))+" tweets")

def auth(l):
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, l)
    return stream



try:
    f = "tweets/tweet.json"
    l = StdOutListener(f, 600)
    l.load_json()
    stream = auth(l)
    stream.filter(track=['corona'])
except KeyboardInterrupt:
    l.save()
