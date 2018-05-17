* auth.py includes all the information needed to interact with the twitter API.
* trending.py shows what's trending in area by WOE_ID (Where on earth). If we use the data structure sets we can use union/difference and intersection.
* timeline.py grabs a given number of tweets from your timeline and JSON dumps them into a new .json file.
* mongo.py, hooking up to mlab, grabbing the info from our database and adding a new row.
* tweet_stream.py live stream, pick number of tweets and keywords.
* read_tweets.py live stream. puts the tweets into mlab.