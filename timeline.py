import tweepy
from auth import api
import json

count = 10

timeline = list(tweepy.Cursor(api.home_timeline).items(count))

for tweet in timeline:
    print(tweet._json['text'])
    
# for tweet in timeline:
#     if tweet._json['retweet_count'] > 1000:
#         print(tweet._json['text'])
        
tweets_list = []
for tweet in timeline:
    tweets_list.append(tweet._json)
        
with open("tweets.json", "w") as f:
    f.write(json.dumps(tweets_list))
    
print("Done")
            
        
        