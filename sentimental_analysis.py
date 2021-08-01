#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021
#ProfiTech Hackathon

#Credit: "Twitter Sentiment Analysis in Python" by NeuralNine

import tweepy
from textblob import TextBlob
import datetime

class TweetAnalyzer:
    '''
    TweetAnalyzer class. Use getStockSentiment to get Tweet sentiment for a specific ticker symbol.
    '''
    def __init__(self, tweet_amount=200):
        '''
        Constructor that sets API keys from twitterkeys.txt
        '''

        # Max number of tweets to check 
        self.tweet_amount = tweet_amount

        # Set API Keys
        mykeys = open('twitterkeys.txt').read().splitlines()

        api_key = mykeys[0]
        api_key_secret = mykeys[1]
        access_token = mykeys[2]
        access_token_secret = mykeys[3]

        auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
        auth_handler.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth_handler)


    def _cleanTweet(self, tweet):
        '''
        Private method used to pre-process tweet text in method getStockSentiment()
        '''
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


    def getStockSentiment(self, ticker_symbol, start_date=datetime.datetime(2021, 7, 30), end_date=datetime.datetime.now()):
        '''
        Returns average polarity (sentiment) of tweets based on parameters provided. 
        -1.0 <= polarity <= 1.0, where more negative values mean more negative sentiment, more positive means more positive sentiment.

        NOTE: The minimum date interval is one day. 
        '''
        polarity = 0
        total = 0

        start_date = start_date.date()
        end_date = end_date.date()

        # Get tweets from API
        tweets = tweepy.Cursor(self.api.search, q=ticker_symbol, lang='en', since=start_date, until=end_date).items(self.tweet_amount)

        #Processing
        for tweet in tweets:
            final_text = self._cleanTweet(tweet)
            
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

#test = TweetAnalyzer()
#print(test.getStockSentiment('GME', datetime.datetime(2021, 7, 31)))

