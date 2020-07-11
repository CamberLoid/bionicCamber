# bionicCamber/api.py
# 存了各种API的对象
import pyrogram, tweepy
import json, redis, logging, sched, time
with open("./auth.json","r") as f:
    auth = json.load(f)

# Pyrogram Auth/API Object
telebot = pyrogram.Client(
    session_name = "bionicCamber",
    bot_token = auth["telegram-bot-token"][0],
    api_id = auth["telegram-user"]["id"],
    api_hash = auth["telegram-user"]["hash"]
    )

altTelebot = pyrogram.Client(
    session_name = "bionicCamberProgressive",
    bot_token = auth["telegram-bot-token"][1],
    api_id = auth["telegram-user"]["id"],
    api_hash = auth["telegram-user"]["hash"]
)

teleuser = pyrogram.Client(
    session_name = "bionicCamberUser",
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

# redisDB = redis.Redis(locals="127.0.0.1", port=13331, db=0) # Deployment
# redisDB = redis.Redis(host="localhost", port=13331, db=1) # Local Env

# Scheduler
scheduler = sched.scheduler(time.time, time.sleep)
