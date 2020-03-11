import socket
import sys
import requests
import json
import tweepy


# override tweepy.StreamListener to add logic to on_status
from tweepy import StreamListener, Stream, OAuthHandler


ACCESS_TOKEN = '620314216-oqeES5scPU2z5w6lJjdvHiCUJGZsD3RKbw9aW7Hp'
ACCESS_SECRET = 'NrI437fzy2PBCkBaY9EZA2K5itpQjBj66WqOLQ5mv2k6Q'
CONSUMER_KEY = '1iWeHX1Zxvh6FBGTj7jV5fYqB'
CONSUMER_SECRET = 'KGdTYXVj2K5XpPne07gZyqQ63oqaXUtAmEUQKBqEIsFg3kithO'


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


##def get_tweets():
##    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
##    query_data = [('language', 'en'), ('locations', '-130,-20,100,50'), ('track', '#')]
##    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
##    response = requests.get(query_url, auth=my_auth, stream=True)
##    print(query_url, response)
##   return response


stream = auth()
stream.filter(track=['basketball'])
