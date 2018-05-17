from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import api, get_auth
from pymongo import MongoClient
from auth import MONGODB_URI
import json

keyword_list=['ruby', 'python', 'java']
limit = 10

DBS_NAME = "first_mongodb"
COLLECTION_NAME = "test4"
MONGODB_URI = "mongodb://root:mongodb@ds237868.mlab.com:37868/first_mongodb"


class MyStreamListener(StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with MongoClient(MONGODB_URI) as conn:
                    collection = conn[DBS_NAME][COLLECTION_NAME]
                    collection.insert(json.loads(data))
                    return True
            except BaseException as e:
                print ("Failed on_data: {0}".format(e))
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True

auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)