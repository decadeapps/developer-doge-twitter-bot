# get you virtual envirnoment roaring
# pipenv shell

# then open up jupyter notebook
# jupyter notebook


# all code below here is done in jupyter notebooks
# they are seperated in chunks to make it easy to execute in jupyter

# import
import tweepy
import webbrowser
import time

# setup your developer account
# make a app in our account
# this will open a tab in your browser to authorize the app
# check if it is the account you want to use
# enter your pin
consumer_key = "yourAccessTokenGoesHere"
consumer_secret = "yourSecretAccessGoesHere"
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pint_input = input("what's the pin value? ")
auth.get_access_token(user_pint_input)

# auth and wait on limits with notifications
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# this you
me = api.me()

# be sure to double check it is the correct account you want to use (easy to miss)
print(me.screen_name)

# enter your search term here as a string called search
search = 'trendyhashtag'

# the number of likes or retweets
numberOfTweets = 150

# time (in seconds) before the next like
timeBetween = 150

# here is the meat and potatoes or the loop function for the actual bot action
# swear there is a good joke here for milk and cereal and loops or something but... anyways
# check out the tweepy documentation to peice together all kinds of stuffz 

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        # this string prints whenever you like a tweet
        print(search + ' has been liked')
        
        # you can substitue favorite for retweet here
        tweet.favorite()
        # have you seen tenet ? such a good movie
        time.sleep(timeBetween)

    # get an error code back so you know
    # currenlty lots of 139 codes but it seems to be working otherwise
    except tweepy.TweepError as e:
            print(e.reason)
    except StopIteration:
                break
    
# hope all this helps you make you own twitter bot
# let me know what you think. I would love to build upon this more with others!