# bionicCamber/api.py
# 存了各种API的对象
import pyrogram, tweepy
import json
with open("./auth.json","r") as f:
    auth = json.load(f)

# Pyrogram Auth/API Object
telebot = pyrogram.Client(
    session_name = "bionicCamber",
    bot_token = auth["telegram-bot-token"],
    api_id = auth["telegram-user"]["id"],
    api_hash = auth["telegram-user"]["hash"]
    )

# tweepy Auth/API Object
tweetauth = tweepy.OAuthHandler(
    auth["twitter"]["consumer_key"], 
    auth["twitter"]["consumer_secret"])
tweetauth.set_access_token(
    auth["twitter"]["access_token"], 
    auth["twitter"]["access_secret"])
tweetapi = tweepy.API(tweetauth)