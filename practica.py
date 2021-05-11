import tweepy
import json
'''
api_key = "JKoWI5IEv9GOJp0FNj5kjFeOi"
api_secret = "4hiK1oVrDf1puqoFKzlADUIlmYp1PDhWY6Qrv6sSSR7drHnsiF"
callback_uri = "oob"
auth = tweepy.OAuthHandler(api_key, api_secret, callback_uri)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

result = api.search(["#diablo","#Diablo","#DIABLO"], lang="en", count=100, tweet_mode="extended")

f = open("tweet.txt", "w")
f.write(json.dumps(result))
f.close()
'''

f = open("tweet.txt", "r")
tw = json.loads(f.read())

print(len(tw["statuses"]))
for x in tw["statuses"]:
    print("\n")
    print(x["user"]["name"])
    print(x["full_text"])

