#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021

#Credit: "Twitter Sentiment Analysis in Python" by NeuralNine

import tweepy
from textblob import TextBlob
import datetime

def cleanTweet(tweet):
    final_text = tweet.text.replace('RT', '')
    #Remove starting username tag
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position + 2 :]
    #Remove remaining username tags
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position + 1 :]
    return final_text

def stockSentiment(tweets):
    polarity = 0
    total = 0

    #Processing
    for tweet in tweets:
        final_text = cleanTweet(tweet)
        
        #Analyze sentiment of tweet
        analysis = TextBlob(final_text)
        tweet_polarity = analysis.polarity

        # For each tweet, -1.0 <= tweet_polarity <= 1.0. The more negative the polarity, the more negative the sentiment.
        # The more positive the polarity, the more positive the sentiment
        polarity += tweet_polarity
        total += 1

    # -1.0 <= avg_polarity <= 1.0, larger magnitudes mean a greater positive or negative sentiment
    avg_polarity = polarity/total

    return avg_polarity

mykeys = open('twitterkeys.txt').read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

#User inputs the stock to analyze
search_term = input('Enter a stock ticker (ex. GME): ')
tweet_amount = 200 #only look at 200 tweets

#Filter through the tweets between the two dates (not including time).
start_date = datetime.datetime(2021, 7, 30).date()
end_date = datetime.datetime.now().date()

tweets = tweepy.Cursor(api.search, q=search_term, lang='en', since=start_date, until=end_date).items(tweet_amount)

polarity = stockSentiment(tweets)

#Output sentiment analysis
print(f"The average polarity of {search_term} is: {polarity}")
#print(f"Number of positive tweets: {positive_tweets}")
#print(f"Number of negative tweets: {negative_tweets}")
#print(f"Number of neutral tweets: {neutral_tweets}")

