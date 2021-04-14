import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# To view twitter home timline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# To display all followers name
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

#tweet liker bot
search_tweet = 'Python'
numbersOfTweets = 5

for tweet in tweepy.Cursor(api.search,search_tweet).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# #To print the name of all followers
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)

# #To follow back a specific follower(or this can be modified to follow back many no of followers as well.)
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'username_of_follower':
        follower.follow()
        break