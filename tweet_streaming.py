import os
from subprocess import Popen

from dotenv import load_dotenv
from tweepy import StreamListener, Stream, OAuthHandler

from hdfs_sender import HDFSSender

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
TCP_IP = "localhost"
TCP_PORT = 9009


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def __init__(self, f):
        self._f = f

    def on_data(self, data):
        print(data)
        f.write(data + "\n")
        return True

    def on_error(self, status):
        print(status)


def auth(f):
    l = StdOutListener(f)
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, l)
    return stream


sender = HDFSSender("tweet.json", "out.json", 5)
sender.start()
f = open("tweet.json", "a")
stream = auth(f)
stream.filter(track=['corona'])
print("daroit")
f.close()
