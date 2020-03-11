import os
import socket
import sys
import requests
import json
import tweepy

# override tweepy.StreamListener to add logic to on_status
from dotenv import load_dotenv
from tweepy import StreamListener, Stream, OAuthHandler

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


def auth():
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = Stream(auth, l)
    return stream


stream = auth()
stream.filter(track=['coronavirus'])
