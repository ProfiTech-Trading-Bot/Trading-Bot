#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021

#Credit: "Twitter Sentiment Analysis in Python" by NeuralNine

import tweepy
from textblob import TextBlob
import datetime

mykeys = open('twitterkeys.txt').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

#user inputs the stock to analyze
search_term = input('Enter a stock ticker (ex. GME): ')
tweet_amount = 200 #only look at 200 tweets

# Filter through the tweets between the two dates (not including time).
start_date = datetime.datetime(2021, 7, 30).date()
end_date = datetime.datetime.now().date()

tweets = tweepy.Cursor(api.search, q=search_term, lang='en', since=start_date, until=end_date).items(tweet_amount)

polarity = 0
positive_tweets = 0
neutral_tweets = 0
negative_tweets = 0

#clean tweet
for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    
    #remove starting username tag
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position + 2 :]
    #remove remaining username tags
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position + 1 :]

    #analyze sentiment of tweet
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    polarity += tweet_polarity

    #determine if tweet was positive, neutral, or negative, and count it 
    if tweet_polarity > 0:
        positive_tweets += 1
    elif tweet_polarity < 0:
        negative_tweets += 1
    else:
        neutral_tweets += 1

    print((tweet.created_at).date())
    print(final_text)

#output sentiment analysis
print(f"The polarity of {search_term} is: {polarity}")
print(f"Number of positive tweets: {positive_tweets}")
print(f"Number of negative tweets: {negative_tweets}")
print(f"Number of neutral tweets: {neutral_tweets}")
