import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

consumer_key = "Rwguik16JSaMutUL6hiT"
consumer_secret = "Nzp9GaeEZZ0r4tsChAuE9EH4K6zR3jLeVM8zkC34PJHSDcB9F0"
access_key = "1610157465567465472-aEptW7lNIwZ6AwVpyudx1SZoDFsC03"
access_secret = "yqZwohhiowh9sYYQZ4vcSoNjGbmSl7OQ3NvzD6Yv4YzyP"

# Twitter Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Creating an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@_fels1',
                           count=200,
                           include_rts=False,
                           tweet_mode='extended'
                           )

for tweet in tweets:
    print(tweet.full_text)
