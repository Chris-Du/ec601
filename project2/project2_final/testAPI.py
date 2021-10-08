#Peiliang Du 
#ec601 testAPI.py

import json
import tweepy #https://github.com/tweepy/tweepy

from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_data_tweet(screen_name):
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    usr = api.get_user(screen_name)
    stat = api.user_timeline(screen_name, count=5)

    print("Screen Name: " + usr.screen_name)
    print("Location: " + str(usr.location))
    print("Created on: " + str(usr.created_at))
    print("Followers count: " + str(usr.followers_count))
    print("Friends count: " + str(usr.friends_count))
    print("Listed count: " + str(usr.listed_count))
    print("Friends count: " + str(usr.friends_count))
    print("Favorites count: " + str(usr.favourites_count))
    print("Account language: " + str(usr.lang))

    for i in stat:
        #print(i.text, end = "\n\n")
        text = i.text
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        print("Text: {}".format(i.text))
        print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

if __name__ == "__main__":
    get_data_tweet("@FCBayern")