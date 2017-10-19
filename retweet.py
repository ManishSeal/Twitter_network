import json
import twitter  as twitter_api
import Twitter_api_credentials as api
twitter_id= []
with open('#fakenews20171019-110144.json', 'r') as fh:
    tweets = json.load(fh)
    for tweet in tweets:
        print(tweet['text'])
        print (tweet['id'])
        twitter_id.append(tweet['id'])

