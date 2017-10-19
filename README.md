# Twitter_network
## Setting up the credentials as Environment variables:
In order to set up the credentials, first get them from your Twitter account and save them at a secure place. Then export them as environmental variables. To do this, type in the **terminal**:

export access_token='*YOUR ACCESS TOKEN*'

export consumer_key='*YOUR ACCESS TOKEN*'

export consumer_secret='*YOUR ACCESS TOKEN*'

export access_token_secret='*YOUR ACCESS TOKEN*'
## To run the code
python twitter_streaming.py > twitter_data.txt
## To search with a certain hashtag
Modify the following line(s) of code:

stream.filter(track=['**insert your hashtag(s) here**'])

