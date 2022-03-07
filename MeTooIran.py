import tweepy
from tweepy import OAuthHandler
import pandas as pd


access_token = ''
access_token_secret = ''
API_key = ''
API_key_secret = ''


auth = tweepy.OAuthHandler(API_key, API_key_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []

count = 1


for tweet in tweepy.Cursor(api.search_full_archive, label= "use your own label", fromDate="200608081010", query="Me_Too_Iran").items(50000):
    
    print(count)
    count += 1

    try: 
        data = [tweet.created_at, tweet.id, tweet.text,
tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
        data = tuple(data)
        tweets.append(data)
        

    except tweepy.TweepError as e:
        print(e.reason)
        continue

    except StopIteration:
        break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])

df.to_csv(path_or_buf = 'Yourpath.csv', index=False)