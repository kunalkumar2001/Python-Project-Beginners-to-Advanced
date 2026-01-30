import tweepy
import pandas as pd

BEARER_TOKEN = "********************************************************************************"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

username = "elonmusk"

# Get user ID
user = client.get_user(username=username)
user_id = user.data.id

# Fetch tweets
tweets = client.get_users_tweets(
    id=user_id,
    max_results=10,
    tweet_fields=["created_at", "public_metrics"]
)

data = []

if tweets.data:
    for tweet in tweets.data:
        data.append({
            "date": tweet.created_at,
            "tweet": tweet.text,
            "likes": tweet.public_metrics["like_count"],
            "retweets": tweet.public_metrics["retweet_count"]
        })

df = pd.DataFrame(data)
df.to_csv("tweets_api.csv", index=False)
print("✅ Tweets saved to tweets_api.csv")
