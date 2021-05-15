import tweepy
import json
import socket
import sys
import requests


api_key = "JKoWI5IEv9GOJp0FNj5kjFeOi"
api_secret = "4hiK1oVrDf1puqoFKzlADUIlmYp1PDhWY6Qrv6sSSR7drHnsiF"
callback_uri = "oob"
auth = tweepy.OAuthHandler(api_key, api_secret, callback_uri)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

result = api.search(["#EuroEnsayos15M"], lang="es", count=100, tweet_mode="extended")

f = open("tweet.txt", "w")
f.write(json.dumps(result))
f.close()



def send_tweets_to_spark(full_tweet, tcp_connection):
    try:
        print ("------------------------------------------")
        print("Text: " + full_tweet)
        print(tcp_connection.send(full_tweet.encode('utf-8')))
    except:
        e = sys.exc_info()[0]
        print("Error: %s" % e)

TCP_IP = "localhost"
TCP_PORT = 10002
conn = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print("Waiting for TCP connection...")
conn, addr = s.accept()

f = open("tweet.txt", "r")
tw = json.loads(f.read())

for x in tw["statuses"]:
    send_tweets_to_spark(x["full_text"]+"\n", conn)

input("Close")