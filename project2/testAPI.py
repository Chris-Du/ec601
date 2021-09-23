#Peiliang Du 
#ec601 testAPI.py

import json
import tweepy #https://github.com/tweepy/tweepy

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    usr = api.get_user(screen_name)

    print("Screen Name: " + usr.screen_name)
    print("Location: " + str(usr.location))
    print("Created on: " + str(usr.created_at))
    print("Followers count: " + str(usr.followers_count))
    print("Friends count: " + str(usr.friends_count))
    print("Listed count: " + str(usr.listed_count))
    print("Friends count: " + str(usr.friends_count))
    print("Favorites count: " + str(usr.favourites_count))
    print("Account language: " + str(usr.lang))


if __name__ == "__main__":
    get_all_tweets("@FCBayern")